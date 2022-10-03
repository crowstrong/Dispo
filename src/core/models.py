from django.db import models


class Cargo(models.Model):
    CARGO_TYPE = (
        ("AUTOMOBILE GOODS", "Automobile Goods"),
        ("INDUSTRY", "Industry"),
        ("INDUSTRY ADR", "Industry ADR"),
        ("INDUSTRY TEMP", "Industry Temp"),
        ("INDUSTRY TEMP ADR", "Industry Temp ADR"),
        ("CONSUMER GOODS", "Consumer Goods"),
        ("FROZEN GOODS", "Frozen Goods"),
        ("FROZEN FOOD", "Frozen Food"),
        ("DRY FOOD", "Dry Food"),
        ("FRUITS & VEGETABLES", "Fruits & Vegetables"),
        ("PET FOOD", "Pet Food"),
        ("AIR FREIGHT", "Air Freight"),
        ("WASTE/GARBAGE", "Waste/Garbage"),
        ("PHARMACY", "Pharmacy"),
        ("EMPTIES", "Empties"),
        ("COLLECTIBLE GOODS", "Collectible Goods"),
        ("COLLECTIBLE GOODS ADR", "Collectible Goods ADR"),
        ("COLLECTIBLE GOODS TEMP", "Collectible Goods Temp"),
        ("COLLECTIBLE GOODS TEMP ADR", "Collectible Goods Temp ADR"),
        ("FURNITURE", "Furniture"),
    )
    ARD_CLASSES = [
        ('Class 1: Explosives', (
            ('1.1', '1.1'),
            ('1.2', '1.2'),
            ('1.3', '1.3'),
            ('1.5', '1.4'),
            ('1.5', '1.5'),
            ('1.6', '1.6'),
        )
         ),
        ('Class 2: Gases', (
            ('2.1', '2.1'),
            ('2.2', '2.2'),
            ('2.3', '2.3'),
        )
         ),
        ('Class 3: Flammable Liquids', (
            ('3', '3'),
        )
         ),
        ('Class 4: Flammable Solids', (
            ('4.1', '4.1'),
            ('4.2', '4.2'),
            ('4.3', '4.3'),
        )
         ),
        ('Class 5: Oxidizing Substances and Organic Peroxides', (
            ('5.1', '5.1'),
            ('5.2', '5.2'),
        )
         ),
        ('Class 6: Toxic and Infectious Substances', (
            ('6.1', '6.1'),
            ('6.2', '6.2'),
        )
         ),
        ('Class 7: Radioactive material', (
            ('7', '7'),
        )
         ),
        ('Class 8: Corrosive substances', (
            ('8', '8'),
        )
         ),
        ('Class 9: Miscellaneous dangerous substances and articles', (
            ('Packing group I', 'Packing group I'),
            ('Packing group II', 'Packing group II'),
            ('Packing group III', 'Packing group III'),
        )
         ),
    ]
    WASTE_TYPES = (
        ("MIXED", 'Mixed'),
        ("PAPER", "Paper"),
        ("SECONDHAND", "SecondHand"),
        ("E-WASTE", "E-Waste"),
        ("GLASS", "Glass"),
        ("METAL", "Metal"),
        ("ORGANIC", "Organic"),
        ("BATTERIES", "Batteries"),
        ("LIGHT BULBS", "Light Bulbs"),

    )
    VEHICLE_TYPES = (
        ("CAR CARRIER", "Car Carrier"),
        ("VAN", "Van"),
        ("REFRIGERATOR", "Refrigerator"),
        ("REFRIGERATOR/DOUBLE-DECK", "Refrigerator/Double-Deck"),
        ("REFRIGERATOR/BI-TEMP", "Refrigerator/Bi-Temp"),
        ("CURTAIN TRAILER", "Curtain Trailer"),
        ("MEGA TRAILER", "Mega Trailer"),
        ("TIPPER", "Tipper"),
        ("BOX TRAILER", "Box Trailer"),
        ("CURTAIN ROLLER BED TRAILER", "Curtain Roller Bed Trailer"),
        ("BOX ROLLER BED TRAILER", "Box Roller Bed Trailer"),
        ("REFRIGERATOR ROLLER BED TRAILER", "Refrigerator Roller Bed Trailer"),
        ("CONTAINER TRAILER", "Container Trailer"),
        ("TANKER", "Tanker"),
        ("INTERMODAL", "Intermodal"),

    )
