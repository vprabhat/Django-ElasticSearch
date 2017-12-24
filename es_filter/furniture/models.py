from django.db import models
from .choices import *
from django.utils import timezone
# Create your models here.
# from filtering.signal_handlers import index_post


models.options.DEFAULT_NAMES = models.options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping'
)

class Furniture(models.Model):
    name = models.TextField()
    brand = models.CharField(max_length=100)
    price_base_unit = models.IntegerField()
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=5)


class Sofa(Furniture):
    furniture_type = models.CharField(choices=SOFA_TYPE_CHOICES, max_length=5)
    material = models.CharField(choices=SOFA_MATERIAL_CHOICES, max_length=2)
    softness = models.CharField(max_length=2, choices = SOFA_SOFTNESS_CHOICES)

    class Meta:
        es_index_name = 'f-sofa-index'
        es_type_name = 'f_sofa_index'
        es_mapping = {
            "properties": {
                "name": {"type": "text"},
                "condition": {"type": "text"},
                "furniture_type": {"type": "text"},
                "material": {"type": "text"},
                "brand": {"type": "text"},
                "softness": {"type": "text"},
                "price_base_unit": {"type": "long"}
            }
        }


class Bed(Furniture):
    furniture_type = models.CharField(choices=BED_TYPE_CHOICES, max_length=5)
    material = models.CharField(choices=BED_MATERIAL_CHOICES, max_length=2)
    storage = models.CharField(choices = BED_STORAGE_CHOICES, max_length=2)

    class Meta:
        es_index_name = 'f-bed-index'
        es_type_name = 'f_bed_index'
        es_mapping = {
            "properties": {
                "name": {"type": "text"},
                "condition": {"type": "text"},
                "furniture_type": {"type": "text"},
                "material": {"type": "text"},
                "brand": {"type": "text"},
                "storage": {"type": "text"},
                "price_base_unit": {"type": "long"}
            }
        }


class Dining(Furniture):
    furniture_type = models.CharField(choices=DINING_TYPE_CHOICES, max_length=5)
    material = models.CharField(choices=DINING_MATERIAL_CHOICES, max_length=2)

    class Meta:
        es_index_name = 'f-dining-index'
        es_type_name = 'f_dining_index'
        es_mapping = {
            "properties": {
                "name": {"type": "text"},
                "condition": {"type": "text"},
                "furniture_type": {"type": "text"},
                "material": {"type": "text"},
                "brand": {"type": "text"},
                "price_base_unit": {"type": "long"}
            }
        }