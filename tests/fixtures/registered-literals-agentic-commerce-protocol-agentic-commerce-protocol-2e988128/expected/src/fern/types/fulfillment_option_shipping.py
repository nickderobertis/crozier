

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FulfillmentOptionShipping(UniversalBaseModel):
    id: str
    title: str
    subtitle: typing.Optional[str] = None
    carrier: typing.Optional[str] = None
    earliest_delivery_time: typing.Optional[dt.datetime] = None
    latest_delivery_time: typing.Optional[dt.datetime] = None
    subtotal: int
    tax: int
    total: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
