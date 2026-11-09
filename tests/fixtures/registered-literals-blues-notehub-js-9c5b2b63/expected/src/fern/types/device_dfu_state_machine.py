

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_dfu_state_machine_node import DeviceDfuStateMachineNode


class DeviceDfuStateMachine(UniversalBaseModel):
    """
    Represents a single request to update the host or Notecard firmware
    """

    current_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of the firmware that was installed prior to this request
    """

    initiated: typing.Optional[str] = pydantic.Field(default=None)
    """
    RFC3339 datetime of when this update was requested
    """

    requested_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of the firmware that was requested to be installed
    """

    updates: typing.Optional[typing.List[DeviceDfuStateMachineNode]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
