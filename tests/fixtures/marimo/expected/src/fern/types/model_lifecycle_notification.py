

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_lifecycle_notification_message import ModelLifecycleNotificationMessage
from .model_lifecycle_notification_op import ModelLifecycleNotificationOp


class ModelLifecycleNotification(UniversalBaseModel):
    """
    Widget model lifecycle message.

        Mirrors the Jupyter widget comm protocol with open/update/custom/close.

        Attributes:
            model_id: Widget model identifier.
            message: The lifecycle message (open/update/custom/close).
    """

    message: ModelLifecycleNotificationMessage
    model_id: str
    op: ModelLifecycleNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
