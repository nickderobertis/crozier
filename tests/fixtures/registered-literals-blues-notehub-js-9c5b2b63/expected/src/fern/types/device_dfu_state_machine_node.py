

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceDfuStateMachineNode(UniversalBaseModel):
    """
    Represents a single request to update the host or Notecard firmware
    """

    datetime: typing.Optional[str] = pydantic.Field(default=None)
    """
    RFC3339 compatible datetime of when this status update happened
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional information
    """

    phase: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phase for this step in the firmware update process
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status for this step in the firmware update process
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
