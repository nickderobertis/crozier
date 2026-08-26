

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interrupted_notification_op import InterruptedNotificationOp


class InterruptedNotification(UniversalBaseModel):
    """
    Kernel was interrupted by user (SIGINT/Ctrl+C).
    """

    op: InterruptedNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
