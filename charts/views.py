from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django import forms
import django_excel as excel
from django.db.models import Count, Sum, QuerySet, Q
from django_pivot.pivot import pivot

from charts.forms import ChartsForm
from charts.models import Question, Choice, Chart
from datetime import date, timedelta


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "xlsx")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    context = RequestContext(request)
    qs = Chart.objects.all()
    return render(request, 'charts/home.html',
                              {'form': form, 'context': context, 'qs': qs})


def download(request):
    sheet = excel.pe.Sheet([[1, 2],[3, 4]])
    return excel.make_response(sheet, "xlsx")


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        def choice_func(row):
            q = Chart.objects.filter(slug=row[0])[0]
            row[0] = q
            return row


        if form.is_valid():

            request.FILES["file"].save_book_to_database(
                models=[Chart],
                initializers=[None, choice_func],
                    # ["name", "date", "field_0", 'field_1', 'field_2', 'field_3', 'field_4', 'field_5', 'field_6',
                    #  'field_7', 'field_8',
                    #  'field_9', 'field_10', 'field_11', 'field_12', 'field_13', 'field_14', 'field_15', 'field_16',
                    #  'field_17', 'field_18',
                    #  'field_19', 'field_20', 'field_21', 'field_22', 'field_23'],
            )
            return redirect("charts:upload")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        "charts/upload_form.html",
        {
            "form": form,
            "title": "Import excel data into database example",
            "header": "Please upload sample-data.xls:",
        },
    )

def chart_test(request):

    qs = 0
    qs_pivot = 0
    form = ChartsForm(request.POST)
    if form.is_valid():
        dt = form.cleaned_data.get('qwe')
        dt = dt.split('-')[1]
        print(dt)
        qs = Chart.objects.filter()
        print(Chart.objects.filter(date__month=dt))
        print(form.cleaned_data.get('qwe'))
        qs_pivot = pivot(qs, 'name_q', 'date', 'dcount')

    else:
        form = ChartsForm()

    return render(request, 'charts/home.html', {'qs': qs, 'form': form})
