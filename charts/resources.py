from import_export import resources
from .models import Chart


class ChartResource(resources.ModelResource):
    class Meta:
        model = Chart
        exclude = ('id', )
        import_id_fields = ['name_q', 'date']
