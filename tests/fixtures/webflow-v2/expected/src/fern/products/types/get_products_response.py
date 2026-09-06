

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_products_response_product import GetProductsResponseProduct
from .get_products_response_skus_item import GetProductsResponseSkusItem


class GetProductsResponse(UniversalBaseModel):
    """
    A product and its SKUs.
    """

    product: typing.Optional[GetProductsResponseProduct] = pydantic.Field(default=None)
    """
    The Product object
    """

    skus: typing.Optional[typing.List[GetProductsResponseSkusItem]] = pydantic.Field(default=None)
    """
    A list of SKU Objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
