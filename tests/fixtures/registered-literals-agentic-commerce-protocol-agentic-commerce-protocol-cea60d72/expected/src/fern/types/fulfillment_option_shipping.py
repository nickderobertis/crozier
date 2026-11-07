

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .total import Total


class FulfillmentOptionShipping(UniversalBaseModel):
    id: str
    title: str
    description: typing.Optional[str] = None
    carrier: typing.Optional[str] = None
    earliest_delivery_time: typing.Optional[dt.datetime] = None
    latest_delivery_time: typing.Optional[dt.datetime] = None
    totals: typing.List[Total]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
