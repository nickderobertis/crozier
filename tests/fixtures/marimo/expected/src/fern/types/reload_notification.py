

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reload_notification_op import ReloadNotificationOp


class ReloadNotification(UniversalBaseModel):
    """
    Instructs frontend to reload the page.
    """

    op: ReloadNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
