

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_description_list import LinkDescriptionList
from .product_collection_element_list import ProductCollectionElementList


class ProductCollection(UniversalBaseModel):
    """
    The list of products, with details.
    """

    products: typing.Optional[ProductCollectionElementList] = None
    total_items: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of items.
    """

    total_pages: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of pages.
    """

    links: typing.Optional[LinkDescriptionList] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
