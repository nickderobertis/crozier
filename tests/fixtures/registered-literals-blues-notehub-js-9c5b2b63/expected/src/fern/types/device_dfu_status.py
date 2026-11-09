

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_dfu_state_machine import DeviceDfuStateMachine
from .device_dfu_status_current import DeviceDfuStatusCurrent


class DeviceDfuStatus(UniversalBaseModel):
    current: typing.Optional[DeviceDfuStatusCurrent] = pydantic.Field(default=None)
    """
    Description of the current firmware
    """

    device_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device UID
    """

    dfu_in_progress: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true if there is a DFU currently in progress
    """

    status: typing.Optional[DeviceDfuStateMachine] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
