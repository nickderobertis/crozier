

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base64string import Base64String
from .ui_element_id import UiElementId
from .ui_element_message_notification_op import UiElementMessageNotificationOp


class UiElementMessageNotification(UniversalBaseModel):
    """
    Sends a message to a UI element/widget.

        Attributes:
            ui_element: UI element identifier.
            message: Message payload as dictionary.
            buffers: Optional binary buffers for large data.
    """

    buffers: typing.Optional[typing.List[Base64String]] = None
    message: typing.Dict[str, typing.Any]
    op: UiElementMessageNotificationOp
    ui_element: UiElementId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
