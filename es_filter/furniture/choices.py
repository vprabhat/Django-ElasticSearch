CONDITION_CHOICES = (('U', 'Unboxed'), ('UP', 'Unboxed Plus'), ('LN', 'Like New'),
                     ('GN', 'Gently Used'), ('WU','Well Used'))

SOFA_TYPE_CHOICES = (('S', 'One Seater'), ('SS', 'Two Seater'), ('SSS', 'Three Seater'),
                     ('SET', 'Sofa Set'), ('LS', ('L Shaped Sofa')), ('SB', 'Sofa cum Bed'),
                     ('R', 'Recliners'))
SOFA_MATERIAL_CHOICES = (('U', 'Upholstered'), ('WF', 'Wood Framed'), ('CB', 'Cane/Bamboo'),
                         ('MF', 'Metal Framed'))
SOFA_SOFTNESS_CHOICES = (('SS', 'Super Soft'), ('S', 'Soft'), ('F', 'Firm'))

BED_TYPE_CHOICES = (('QS', 'Queen size beds'), ('KS', 'King Size Beds'), ('SB', 'Single Bed'),
                    ('D', 'Diwans'))
BED_MATERIAL_CHOICES = (('SW', 'Solid Wood'), ('PW', 'Ply Wood'), ('EW', 'Engineering Wood'),
                        ('M', 'Metal Framed'))
BED_STORAGE_CHOICES = (('BD', 'Box/Drawer Storage'), ('HS', 'Hydraulic Storage'), ('NS', 'Non-Storage'))


DINING_TYPE_CHOICES = (('4S', '4 Seater Sets'), ('6S', '6 Seater Sets'), ('DT', 'Dining Tables'))
DINING_MATERIAL_CHOICES = (('G', 'Glass'), ('SMW', 'Seesham/Mango Wood'),
                           ('RPW', 'Rubber/Pine Wood'),('TW', 'Teak Wood'), ('CB', 'Cane Bamboo'))

BRANDS = (('Urban Ladder', 'Urban Ladder'), ('Liv Space','Liv Space'),
          ('Housefull','Housefull'), ('Roman Living','Roman Living'))

def parse(sym, desc):
    return {
        "type": sym.lower(),
        "displayName": desc
    }

DEFAULT_FILTER = [
    {
        "type": "condition", "displayName": "Condition", "childs": [parse(*e) for e in CONDITION_CHOICES],
        }
]

SOFA_FILTERS = [
    {
        "type": "furniture_type", "displayName": "Furniture Type",
        "childs": [parse(*e) for e in SOFA_TYPE_CHOICES],
        },
    {
        "type": "material", "displayName": "Material",
        "childs": [parse(*e) for e in SOFA_MATERIAL_CHOICES],
        },
    {
        "type": "softness", "displayName": "Softness",
        "childs": [parse(*e) for e in SOFA_SOFTNESS_CHOICES],
        }
] + DEFAULT_FILTER

BED_FILTERS = [
    {
        "type": "furniture_type", "displayName": "Furniture Type",
        "childs": [parse(*e) for e in BED_TYPE_CHOICES],
        },
    {
        "type": "material", "displayName": "Material",
        "childs": [parse(*e) for e in BED_MATERIAL_CHOICES],
        },
    {
        "type": "storage", "displayName": "Storage",
        "childs": [parse(*e) for e in BED_STORAGE_CHOICES],
        }
] + DEFAULT_FILTER


DINING_FILTERS = [
    {
        "type": "furniture_type", "displayName": "Furniture Type",
        "childs": [parse(*e) for e in DINING_TYPE_CHOICES],
        },
    {
        "type": "material", "displayName": "Material",
        "childs": [parse(*e) for e in DINING_MATERIAL_CHOICES],
        },
] + DEFAULT_FILTER