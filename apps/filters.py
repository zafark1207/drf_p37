from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet

from apps.models import Post


# from apps.models import Post
#
#
# # from apps.models import Student
# #
# #
class PostFilter(FilterSet):
    min_created_at = NumberFilter(field_name='created_at', lookup_expr='gte')
    max_created_at = NumberFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ('tags', 'category')