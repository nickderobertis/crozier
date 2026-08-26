

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .startup_logs_notification_op import StartupLogsNotificationOp
from .startup_logs_notification_status import StartupLogsNotificationStatus


class StartupLogsNotification(UniversalBaseModel):
    """
    Streaming kernel startup logs.

        Attributes:
            content: Log content to display.
            status: Stream status (start/append/done).
    """

    content: str
    op: StartupLogsNotificationOp
    status: StartupLogsNotificationStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
