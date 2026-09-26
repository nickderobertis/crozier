

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .order_message_type import OrderMessageType
from .order_order import OrderOrder


class Order(BaseMessageType):
    message_type: typing.Optional[OrderMessageType] = pydantic.Field(default=None)
    """
    The type of message to send.
    """

    order: OrderOrder

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
