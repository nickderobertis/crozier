

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dfu_state_mode import DfuStateMode
from .dfu_state_type import DfuStateType


class DfuState(UniversalBaseModel):
    began: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time when the DFU began
    """

    crc32: typing.Optional[int] = pydantic.Field(default=None)
    """
    Used for image verification
    """

    errors: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of consecutive errors the DFU process has encountered
    """

    file: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware filename
    """

    length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Length of firmware file
    """

    md5: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used for image verification
    """

    mode: typing.Optional[DfuStateMode] = pydantic.Field(default=None)
    """
    * "idle"          - nothing downloading or downloaded
    * "error"         - halted and in the error state
    * "downloading"   - transferring data from cloud to module
    * "sideloading"   - transferring data via request to module
    * "ready"         - DFU data is ready/verified and waiting on external storage
    * "ready-retry"   - DFU data is ready/verified and retrying
    * "updating"      - currently updating
    * "completed"     - DFU is done successfully
    """

    read: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount the notecard has read of the image from notehub
    """

    retry: typing.Optional[int] = pydantic.Field(default=None)
    """
    Value of _fw_retry environment var at time of DFU initialization
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status message
    """

    type: typing.Optional[DfuStateType] = None
    updated: typing.Optional[int] = pydantic.Field(default=None)
    """
    Last updated timestamp
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last known version, which is generally a JSON object contained within the firmware image
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
