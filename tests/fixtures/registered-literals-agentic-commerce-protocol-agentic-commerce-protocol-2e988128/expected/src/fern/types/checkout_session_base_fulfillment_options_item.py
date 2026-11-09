

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CheckoutSessionBaseFulfillmentOptionsItem_Shipping(UniversalBaseModel):
    type: typing.Literal["shipping"] = "shipping"
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


class CheckoutSessionBaseFulfillmentOptionsItem_Digital(UniversalBaseModel):
    type: typing.Literal["digital"] = "digital"
    id: str
    title: str
    subtitle: typing.Optional[str] = None
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


CheckoutSessionBaseFulfillmentOptionsItem = typing_extensions.Annotated[
    typing.Union[CheckoutSessionBaseFulfillmentOptionsItem_Shipping, CheckoutSessionBaseFulfillmentOptionsItem_Digital],
    pydantic.Field(discriminator="type"),
]
