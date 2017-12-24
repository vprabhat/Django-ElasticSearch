from elasticsearch.client import IndicesClient
from django.conf import settings
from django.core.management.base import BaseCommand
from elasticsearch.helpers import bulk

from furniture.models import Sofa, Dining, Bed
from furniture.serializers import SofaSerializerES, BedSerializerES, DiningSerializerES


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = IndicesClient(client=settings.ES_CLIENT)
        self.recreate_index(
            client, **{
                'index_name': Sofa._meta.es_index_name,
                'doc_type': Sofa._meta.es_type_name,
                'body': Sofa._meta.es_mapping
            }
        )
        self.push_db_to_index(client, SofaSerializerES, Sofa.objects.all().iterator())

        self.recreate_index(
            client, **{
                'index_name': Bed._meta.es_index_name,
                'doc_type': Bed._meta.es_type_name,
                'body': Bed._meta.es_mapping
            }
        )
        self.push_db_to_index(client, BedSerializerES, Bed.objects.all().iterator())

        self.recreate_index(
            client, **{
                'index_name': Dining._meta.es_index_name,
                'doc_type': Dining._meta.es_type_name,
                'body': Dining._meta.es_mapping
            }
        )
        self.push_db_to_index(client, DiningSerializerES, Dining.objects.all().iterator())

    def recreate_index(self, client, **kwargs):
        if client.exists(kwargs['index_name']):
            client.delete(index=kwargs['index_name'])
        client.create(index=kwargs['index_name'], params={"timeout":"30s"})
        client.put_mapping(
            doc_type=kwargs['doc_type'],
            body=kwargs['body'],
            index=kwargs['index_name'], params={'timeout':"30s"}
        )

    def push_db_to_index(self, client, serializer, o_iterator):
        data = [
            self.convert_for_bulk(s, serializer, 'create') for s in o_iterator
        ]
        bulk(client=settings.ES_CLIENT, actions=data, stats_only=True)

    def convert_for_bulk(self, _object, serializer, action=None):
        data = serializer(_object).data
        metadata = {
            "_op_type": action,
            "_index": _object._meta.es_index_name,
            "_type": _object._meta.es_type_name,
        }
        data.update(**metadata)
        return data