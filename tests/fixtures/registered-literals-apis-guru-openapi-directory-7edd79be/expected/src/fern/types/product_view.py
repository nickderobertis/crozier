

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subscription_view import SubscriptionView


class ProductView(UniversalBaseModel):
    created: typing.Optional[dt.datetime] = None
    custom: typing.Optional[typing.Any] = None
    name: typing.Optional[str] = None
    serial: typing.Optional[str] = None
    subscriptions: typing.Optional[typing.List[SubscriptionView]] = None
    updated: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
