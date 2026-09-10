

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .date_time import DateTime
from .link_description_list import LinkDescriptionList
from .product_category import ProductCategory
from .product_type import ProductType


class Product(UniversalBaseModel):
    """
    The product details.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the product.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The product name.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The product description.
    """

    type: typing.Optional[ProductType] = pydantic.Field(default=None)
    """
    The product type. Indicates whether the product is physical or digital goods, or a service.
    """

    category: typing.Optional[ProductCategory] = None
    image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image URL for the product.
    """

    home_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The home page URL for the product.
    """

    create_time: typing.Optional[DateTime] = pydantic.Field(default=None)
    """
    The date and time when the product was created, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6).
    """

    update_time: typing.Optional[DateTime] = pydantic.Field(default=None)
    """
    The date and time when the product was last updated, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6).
    """

    links: typing.Optional[LinkDescriptionList] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
