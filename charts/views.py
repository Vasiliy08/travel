import tablib
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django import forms
import django_excel as excel
from django.db.models import Count, Sum, QuerySet, Q
from django.views.generic import DetailView, UpdateView
from django_pivot.pivot import pivot
from tablib import Dataset

from charts.forms import ChartsForm, ChartFormSet
from charts.models import Question, Choice, Chart
import datetime
import calendar
from import_export import resources
import pprint
import pandas as pd
import tablib
from .resources import ChartResource


# class UploadFileForm(forms.Form):
#     file = forms.FileField()
#
#
# def upload(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             filehandle = request.FILES['file']
#             return excel.make_response(filehandle.get_sheet(), "xlsx")
#         else:
#             return HttpResponseBadRequest()
#     else:
#         form = UploadFileForm()
#     context = RequestContext(request)
#     qs = Chart.objects.all()
#     return render(request, 'charts/upload_form.html',
#                   {'form': form, 'context': context, 'qs': qs})
#
#
# def download(request):
#     sheet = excel.pe.Sheet([[1, 2], [3, 4]])
#     return excel.make_response(sheet, "xlsx")
#

# def import_data(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#
#         def choice_func(row):
#             q = Chart.objects.filter(slug=row[0])[0]
#             row[0] = q
#             return row
#
#
#         if form.is_valid():
#             try:
#                 request.FILES["file"].save_book_to_database(
#                     models=[Chart],
#                     initializers=[None, choice_func]
#                 )
#                 print('Успешно?')
#             except Exception as ex:
#                 print('Не загрузилось?')
#             return redirect("charts:upload")
#
#         else:
#             return HttpResponseBadRequest()
#     else:
#         form = UploadFileForm()
#     return render(
#         request,
#         "charts/upload_form.html",
#         {
#             "form": form,
#             "title": "Import excel data into database example",
#             "header": "Please upload sample-data.xls:",
#         },
#     )
def import_data_to_bd(request):
    if request.method == 'POST':
        person_resource = ChartResource()
        dataset = Dataset()
        new_persons = request.FILES['file']

        imported_data = dataset.load(new_persons.read(), format='xlsx')
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
        print(imported_data)
        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
            messages.success(request, 'Успешно')

        else:
            messages.error(request, 'Упс, что-то пошло не так')

    return render(request, 'charts/excel.html')

def chart_test(request):
    qs_lst = []
    lst = []
    form = ChartsForm(request.POST)
    date_for_detail = []

    if form.is_valid():
        # Достаём дату с формы
        dt_date = form.cleaned_data.get('qwe')
        dt_month = dt_date.split('-')[1]
        dt_year = dt_date.split('-')[0]
        dt_day = dt_date.split('-')[2]
        qs_fact_in_bd = Chart.objects.filter(Q(date__month=dt_month) & Q(date__year=dt_year))

        qs_pivot = pivot(qs_fact_in_bd, 'name_q', 'date', 'dcount')
        # qs_name = Chart.objects.values('name_q').order_by('name_q').distinct('name_q')
        qs_name1 = [i['name_q'] for i in qs_pivot]

        list_date = list(map(int, str(dt_date).split('-')))
        count_day = calendar.monthrange(list_date[0], list_date[1])[1]
        first_day_in_month = datetime.date(list_date[0], list_date[1], 1)

        for i in range(count_day):
            qs_lst.append(first_day_in_month)
            first_day_in_month = first_day_in_month + datetime.timedelta(days=1)

        dct = {}
        for i in qs_lst:
            dct.setdefault(str(i), 0)

        lst = {}
        for name in qs_name1:
            lst.setdefault(name, dct)

        for piv in qs_pivot:
            for lst_key, lst_val in lst.items():
                if piv['name_q'] == lst_key:
                    a = {k: v for k, v in piv.items() if v is not None and k != 'name_q'}
                    lst[lst_key] = lst_val | a

        # Дата для детализации
        date_for_detail = '-'.join((dt_year, dt_month, dt_day))


    else:
        form = ChartsForm()

    return render(request, 'charts/home.html', {'form': form, 'qs_lst': qs_lst, 'lst': lst, 'date_for_detail': date_for_detail})


# class ChartDetailView(DetailView):
#     model = Chart
#     template_name = 'charts/detail.html'
#     slug_url_kwarg = 'post_str'
#     slug_field = 'name_q'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['qs'] = context
#         return context


def chart_detail(request, post_str, date_str):

    qs_lst = []
    qs_dct = {post_str: {}}

    # Достаём дату с формы
    dt_month = date_str.split('-')[1]
    dt_year = date_str.split('-')[0]
    dt_day = date_str.split('-')[2]
    qs_fact_in_bd = Chart.objects.filter(Q(name_q=post_str) & Q(date__month=dt_month) & Q(date__year=dt_year)).values()

    print(qs_fact_in_bd)

    for qs in qs_fact_in_bd:
        for key, val in qs.items():
            if key not in ['id', 'name_q', 'date', 'dcount']:
                qs_dct[post_str].setdefault(key, []).append(val)

    print(qs_dct)

    list_date = list(map(int, str(date_str).split('-')))
    count_day = calendar.monthrange(list_date[0], list_date[1])[1]
    first_day_in_month = datetime.date(list_date[0], list_date[1], 1)

    for i in range(count_day):
        qs_lst.append(first_day_in_month)
        first_day_in_month = first_day_in_month + datetime.timedelta(days=1)

    print(qs_lst)

    # qs_pivot = pivot(qs_fact_in_bd, 'name_q', 'date', 'dcount')
    # # qs_name = Chart.objects.values('name_q').order_by('name_q').distinct('name_q')
    # qs_name1 = [i['name_q'] for i in qs_pivot]
    #
    # list_date = list(map(int, str(date_str).split('-')))
    # count_day = calendar.monthrange(list_date[0], list_date[1])[1]
    # first_day_in_month = datetime.date(list_date[0], list_date[1], 1)

    # print(list_date)
    # print(count_day)
    # print(first_day_in_month)
    # print(qs_name1)
    # print(qs_pivot)
    # print(qs_fact_in_bd)

    # for i in range(count_day):
    #     qs_lst.append(first_day_in_month)
    #     first_day_in_month = first_day_in_month + datetime.timedelta(days=1)
    #
    # dct = {}
    # for i in qs_lst:
    #     dct.setdefault(str(i), 0)
    #
    # lst = {}
    # for name in qs_name1:
    #     lst.setdefault(name, dct)
    #
    # for piv in qs_pivot:
    #     for lst_key, lst_val in lst.items():
    #         if piv['name_q'] == lst_key:
    #             a = {k: v for k, v in piv.items() if v is not None and k != 'name_q'}
    #             lst[lst_key] = lst_val | a

    return render(request, 'charts/detail.html', {'qs_lst': qs_lst})





def create_chart(request):
    if request.method == 'POST':
        formset = ChartFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            print(formset.cleaned_data)
            for form in formset.cleaned_data:
                print(form)
                Chart.objects.create(**form)
    else:
        formset = ChartFormSet()
    return render(request, 'charts/chart_create.html', {'formset': formset})