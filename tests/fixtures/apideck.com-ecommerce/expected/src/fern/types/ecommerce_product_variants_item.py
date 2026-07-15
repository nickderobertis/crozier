

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecommerce_product_variants_item_images_item import EcommerceProductVariantsItemImagesItem
from .ecommerce_product_variants_item_options_item import EcommerceProductVariantsItemOptionsItem


class EcommerceProductVariantsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the variant of the product.
    """

    images: typing.Optional[typing.List[EcommerceProductVariantsItemImagesItem]] = None
    inventory_quantity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The quantity of the variant in stock.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the variant, used for displaying to customers.
    """

    options: typing.Optional[typing.List[EcommerceProductVariantsItemOptionsItem]] = None
    price: typing.Optional[str] = pydantic.Field(default=None)
    """
    The price of the variant.
    """

    sku: typing.Optional[str] = pydantic.Field(default=None)
    """
    The stock keeping unit of the variant.
    """

    weight: typing.Optional[str] = pydantic.Field(default=None)
    """
    The weight of the variant.
    """

    weight_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unit of measurement for the weight of the variant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
