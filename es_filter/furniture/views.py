from django.shortcuts import render

# Create your views here.
import json
from django.conf import settings
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .choices import SOFA_FILTERS,BED_FILTERS, DINING_FILTERS
from .models import Sofa, Bed, Dining

# and add two auxiliary views:
client = settings.ES_CLIENT

def home_view(request, *args, **kwargs):
    return render(request, 'index.html')


@api_view(['GET'])
@permission_classes([permissions.AllowAny,])
def get_furniture_filters(request, *args, **kwargs):
    query = request.query_params.get('query')
    if query == 'sofa':
        return Response(SOFA_FILTERS)
    elif query == 'bed':
        return Response(BED_FILTERS)
    elif query == 'dining':
        return Response(DINING_FILTERS)
    else:
        return Response({
            "error_code": "FL01",
            "error_message": "Invalid product category"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
def filtered_furnitures(request, *args, **kwargs):
    #request data
    #"query": {
    #                   "price_base_unit":[],
    #                    "condition":[]
    #               }
    query = request.data.get("query")
    res = client.search(index='f-%s-index'%(kwargs['furniture_type']), size=600,
                        body={"query": gen_es_query(query)})
    return Response(res['hits']['hits'])


def gen_es_query(query):
    if not query:
        return {'match_all': {}}
    filters = []
    for key in query.keys():
        if key == "price_base_unit":
            filters.append({"range":{"price_base_unit":{"gt":min(query['price_base_unit']),
                                                        "lt":max(query['price_base_unit'])}}})
        else:
            filters.append({"terms":{key:query[key]}})
    return {
        "bool":{
            "filter":{
                "bool":{
                    "must": filters
                }
            }
        }
    }