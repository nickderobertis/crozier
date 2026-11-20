

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .product_order_address import ProductOrderAddress


class ProductOrder(UniversalBaseModel):
    sku: typing.Optional[str] = None
    quantity: typing.Optional[float] = None
    address: typing.Optional[ProductOrderAddress] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
