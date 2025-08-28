from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .serializers import (
    PropertySerializer
)

from .models import (
    Property
)


@cache_page(60 * 15)
def property_list(request):
    queryset = Property.objects.all()
    serializer = PropertySerializer(queryset, many=True)

    return JsonResponse({'properties': serializer.data})
