

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .product_status import ProductStatus


class Product(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    status: typing.Optional[ProductStatus] = None
    currency: typing.Optional[str] = None
    price: typing.Optional[float] = None
    url: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
