from random import randint

from model_mommy import mommy
from django.core.management.base import BaseCommand
from furniture.models import Sofa, Bed, Dining
from furniture.choices import *

brands = ['Urban Ladder', 'Liv Space', 'Housefull', 'Roman Living']


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clear()
        self.make_furnitures()

    def clear(self):
        Sofa.objects.all().delete()
        Bed.objects.all().delete()
        Dining.objects.all().delete()

    def make_furnitures(self):
        self.make_sofas()
        self.make_beds()
        self.make_dinings()

    def make_sofas(self):
        for num in range(100):
            brand = brands[randint(0, len(brands) - 1)]
            f_type, f_desc = SOFA_TYPE_CHOICES[randint(0, len(SOFA_TYPE_CHOICES) - 1)]
            mommy.make(Sofa,
                       name="%s %s" % (brand, f_desc),
                       brand=brand,
                       condition=get_value(CONDITION_CHOICES[randint(0, len(CONDITION_CHOICES) - 1)]),
                       price_base_unit=randint(2000, 15000),
                       furniture_type=f_type,
                       material=get_value(SOFA_MATERIAL_CHOICES[randint(0, len(SOFA_MATERIAL_CHOICES) - 1)]),
                       softness=get_value(SOFA_SOFTNESS_CHOICES[randint(0, len(SOFA_SOFTNESS_CHOICES) - 1)]))

    def make_beds(self):
        for num in range(100):
            brand = brands[randint(0, len(brands) - 1)]
            f_type, f_desc = BED_TYPE_CHOICES[randint(0, len(BED_TYPE_CHOICES) - 1)]
            mommy.make(Bed,
                       name="%s %s" % (brand, f_desc),
                       brand=brand,
                       condition=get_value(CONDITION_CHOICES[randint(0, len(CONDITION_CHOICES) - 1)]),
                       price_base_unit=randint(2000, 15000),
                       furniture_type=f_type,
                       material=get_value(BED_MATERIAL_CHOICES[randint(0, len(BED_MATERIAL_CHOICES) - 1)]),
                       storage=get_value(BED_STORAGE_CHOICES[randint(0, len(BED_STORAGE_CHOICES) - 1)]))

    def make_dinings(self):
        for num in range(100):
            brand = brands[randint(0, len(brands) - 1)]
            f_type, f_desc = DINING_TYPE_CHOICES[randint(0, len(DINING_TYPE_CHOICES) - 1)]
            mommy.make(Dining,
                       name="%s %s" % (brand, f_desc),
                       brand=brand,
                       condition=get_value(CONDITION_CHOICES[randint(0, len(CONDITION_CHOICES) - 1)]),
                       price_base_unit=randint(2000, 15000),
                       furniture_type=f_type,
                       material=get_value(DINING_MATERIAL_CHOICES[randint(0, len(DINING_MATERIAL_CHOICES) - 1)]))


def get_value(_tuple):
    a,b = _tuple
    return a