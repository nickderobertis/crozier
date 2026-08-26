

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .kernel_startup_error_notification_op import KernelStartupErrorNotificationOp


class KernelStartupErrorNotification(UniversalBaseModel):
    """
    Kernel failed to start.

        Attributes:
            error: Error message describing failure.
    """

    error: str
    op: KernelStartupErrorNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
