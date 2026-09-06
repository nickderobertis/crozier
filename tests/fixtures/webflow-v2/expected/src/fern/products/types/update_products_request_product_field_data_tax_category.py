

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateProductsRequestProductFieldDataTaxCategory(enum.StrEnum):
    """
    Product tax class
    """

    STANDARD_TAXABLE = "standard-taxable"
    STANDARD_EXEMPT = "standard-exempt"
    BOOKS_RELIGIOUS = "books-religious"
    BOOKS_TEXTBOOK = "books-textbook"
    CLOTHING = "clothing"
    CLOTHING_SWIMWEAR = "clothing-swimwear"
    DIGITAL_GOODS = "digital-goods"
    DIGITAL_SERVICE = "digital-service"
    DRUGS_NON_PRESCRIPTION = "drugs-non-prescription"
    DRUGS_PRESCRIPTION = "drugs-prescription"
    FOOD_BOTTLED_WATER = "food-bottled-water"
    FOOD_CANDY = "food-candy"
    FOOD_GROCERIES = "food-groceries"
    FOOD_PREPARED = "food-prepared"
    FOOD_SODA = "food-soda"
    FOOD_SUPPLEMENTS = "food-supplements"
    MAGAZINE_INDIVIDUAL = "magazine-individual"
    MAGAZINE_SUBSCRIPTION = "magazine-subscription"
    SERVICE_ADMISSION = "service-admission"
    SERVICE_ADVERTISING = "service-advertising"
    SERVICE_DRY_CLEANING = "service-dry-cleaning"
    SERVICE_HAIRDRESSING = "service-hairdressing"
    SERVICE_INSTALLATION = "service-installation"
    SERVICE_MISCELLANEOUS = "service-miscellaneous"
    SERVICE_PARKING = "service-parking"
    SERVICE_PRINTING = "service-printing"
    SERVICE_PROFESSIONAL = "service-professional"
    SERVICE_REPAIR = "service-repair"
    SERVICE_TRAINING = "service-training"

    def visit(
        self,
        standard_taxable: typing.Callable[[], T_Result],
        standard_exempt: typing.Callable[[], T_Result],
        books_religious: typing.Callable[[], T_Result],
        books_textbook: typing.Callable[[], T_Result],
        clothing: typing.Callable[[], T_Result],
        clothing_swimwear: typing.Callable[[], T_Result],
        digital_goods: typing.Callable[[], T_Result],
        digital_service: typing.Callable[[], T_Result],
        drugs_non_prescription: typing.Callable[[], T_Result],
        drugs_prescription: typing.Callable[[], T_Result],
        food_bottled_water: typing.Callable[[], T_Result],
        food_candy: typing.Callable[[], T_Result],
        food_groceries: typing.Callable[[], T_Result],
        food_prepared: typing.Callable[[], T_Result],
        food_soda: typing.Callable[[], T_Result],
        food_supplements: typing.Callable[[], T_Result],
        magazine_individual: typing.Callable[[], T_Result],
        magazine_subscription: typing.Callable[[], T_Result],
        service_admission: typing.Callable[[], T_Result],
        service_advertising: typing.Callable[[], T_Result],
        service_dry_cleaning: typing.Callable[[], T_Result],
        service_hairdressing: typing.Callable[[], T_Result],
        service_installation: typing.Callable[[], T_Result],
        service_miscellaneous: typing.Callable[[], T_Result],
        service_parking: typing.Callable[[], T_Result],
        service_printing: typing.Callable[[], T_Result],
        service_professional: typing.Callable[[], T_Result],
        service_repair: typing.Callable[[], T_Result],
        service_training: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateProductsRequestProductFieldDataTaxCategory.STANDARD_TAXABLE:
            return standard_taxable()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.STANDARD_EXEMPT:
            return standard_exempt()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.BOOKS_RELIGIOUS:
            return books_religious()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.BOOKS_TEXTBOOK:
            return books_textbook()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.CLOTHING:
            return clothing()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.CLOTHING_SWIMWEAR:
            return clothing_swimwear()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.DIGITAL_GOODS:
            return digital_goods()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.DIGITAL_SERVICE:
            return digital_service()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.DRUGS_NON_PRESCRIPTION:
            return drugs_non_prescription()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.DRUGS_PRESCRIPTION:
            return drugs_prescription()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.FOOD_BOTTLED_WATER:
            return food_bottled_water()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.FOOD_CANDY:
            return food_candy()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.FOOD_GROCERIES:
            return food_groceries()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.FOOD_PREPARED:
            return food_prepared()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.FOOD_SODA:
            return food_soda()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.FOOD_SUPPLEMENTS:
            return food_supplements()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.MAGAZINE_INDIVIDUAL:
            return magazine_individual()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.MAGAZINE_SUBSCRIPTION:
            return magazine_subscription()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_ADMISSION:
            return service_admission()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_ADVERTISING:
            return service_advertising()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_DRY_CLEANING:
            return service_dry_cleaning()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_HAIRDRESSING:
            return service_hairdressing()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_INSTALLATION:
            return service_installation()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_MISCELLANEOUS:
            return service_miscellaneous()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_PARKING:
            return service_parking()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_PRINTING:
            return service_printing()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_PROFESSIONAL:
            return service_professional()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_REPAIR:
            return service_repair()
        if self is UpdateProductsRequestProductFieldDataTaxCategory.SERVICE_TRAINING:
            return service_training()
