import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    type = django_filters.CharFilter(field_name='type')

    class Meta:
        model = Transaction
        fields = ['start_date', 'end_date', 'type']
