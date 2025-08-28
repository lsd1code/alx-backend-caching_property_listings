from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from .serializers import (
    PropertySerializer
)

from .models import (
    Property
)


@api_view(['GET'])
@cache_page(60*15)
def property_list(request: Request):
    queryset = Property.objects.all()
    serializer = PropertySerializer(queryset, many=True)

    return Response(serializer.data)
