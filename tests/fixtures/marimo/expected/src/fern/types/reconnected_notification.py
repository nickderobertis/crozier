

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reconnected_notification_op import ReconnectedNotificationOp


class ReconnectedNotification(UniversalBaseModel):
    """
    WebSocket reconnection confirmed.
    """

    op: ReconnectedNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
