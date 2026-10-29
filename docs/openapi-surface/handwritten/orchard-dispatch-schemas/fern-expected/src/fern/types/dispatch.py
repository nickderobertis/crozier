

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delivery import Delivery
from .delivery_condition import DeliveryCondition
from .notice import Notice
from .notice_condition import NoticeCondition
from .routing_hint import RoutingHint
from .spare_basket import SpareBasket


class Dispatch(UniversalBaseModel):
    hint: typing.Optional[RoutingHint] = None
    basket: typing.Optional[SpareBasket] = None
    delivery: typing.Optional[Delivery] = None
    delivery_condition: typing.Optional[DeliveryCondition] = None
    notice: typing.Optional[Notice] = None
    notice_condition: typing.Optional[NoticeCondition] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
