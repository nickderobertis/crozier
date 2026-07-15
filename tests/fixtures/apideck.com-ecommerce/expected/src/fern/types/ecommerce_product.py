

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .ecommerce_product_categories_item import EcommerceProductCategoriesItem
from .ecommerce_product_images_item import EcommerceProductImagesItem
from .ecommerce_product_options_item import EcommerceProductOptionsItem
from .ecommerce_product_status import EcommerceProductStatus
from .ecommerce_product_variants_item import EcommerceProductVariantsItem
from .id import Id
from .updated_at import UpdatedAt


class EcommerceProduct(UniversalBaseModel):
    categories: typing.Optional[typing.List[EcommerceProductCategoriesItem]] = pydantic.Field(default=None)
    """
    An array of categories for the product, used for organization and searching.
    """

    created_at: typing.Optional[CreatedAt] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A detailed description of the product.
    """

    id: typing.Optional[Id] = None
    images: typing.Optional[typing.List[EcommerceProductImagesItem]] = pydantic.Field(default=None)
    """
    An array of image URLs for the product.
    """

    inventory_quantity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The quantity of the product in stock.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the product as it should be displayed to customers.
    """

    options: typing.Optional[typing.List[EcommerceProductOptionsItem]] = pydantic.Field(default=None)
    """
    An array of options for the product.
    """

    price: typing.Optional[str] = pydantic.Field(default=None)
    """
    The price of the product.
    """

    sku: typing.Optional[str] = pydantic.Field(default=None)
    """
    The stock keeping unit of the product.
    """

    status: typing.Optional[EcommerceProductStatus] = pydantic.Field(default=None)
    """
    The current status of the product (active or archived).
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of tags for the product, used for organization and searching.
    """

    updated_at: typing.Optional[UpdatedAt] = None
    variants: typing.Optional[typing.List[EcommerceProductVariantsItem]] = None
    weight: typing.Optional[str] = pydantic.Field(default=None)
    """
    The weight of the product.
    """

    weight_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unit of measurement for the weight of the product.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
