

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogStockConversion(UniversalBaseModel):
    """
    Represents the rule of conversion between a stockable [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
    and a non-stockable sell-by or receive-by `CatalogItemVariation` that
    share the same underlying stock.
    """

    nonstockable_quantity: str = pydantic.Field()
    """
    The converted equivalent quantity of the non-stockable [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) 
    in its measurement unit. The `stockable_quantity` value and this `nonstockable_quantity` value together
    define the conversion ratio between stockable item variation and the non-stockable item variation.
    It accepts a decimal number in a string format that can take up to 10 digits before the decimal point
    and up to 5 digits after the decimal point.
    """

    stockable_item_variation_id: str = pydantic.Field()
    """
    References to the stockable [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
    for this stock conversion. Selling, receiving or recounting the non-stockable `CatalogItemVariation` 
    defined with a stock conversion results in adjustments of this stockable `CatalogItemVariation`.
    This immutable field must reference a stockable `CatalogItemVariation`
    that shares the parent [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) of the converted `CatalogItemVariation.`
    """

    stockable_quantity: str = pydantic.Field()
    """
    The quantity of the stockable item variation (as identified by `stockable_item_variation_id`) 
    equivalent to the non-stockable item variation quantity (as specified in `nonstockable_quantity`) 
    as defined by this stock conversion.  It accepts a decimal number in a string format that can take
    up to 10 digits before the decimal point and up to 5 digits after the decimal point.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
