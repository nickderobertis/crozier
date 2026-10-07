

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stop_kernel_command_type import StopKernelCommandType


class StopKernelCommand(UniversalBaseModel):
    """
    Stop kernel execution.

        Signals the kernel to stop processing and shut down gracefully.
        Used when closing a notebook or terminating a session.
    """

    type: StopKernelCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
