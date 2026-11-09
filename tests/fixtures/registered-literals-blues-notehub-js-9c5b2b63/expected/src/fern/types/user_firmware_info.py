

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .current_firmware import CurrentFirmware
from .user_dfu_state_machine import UserDfuStateMachine


class UserFirmwareInfo(UniversalBaseModel):
    current_firmware: typing.Optional[CurrentFirmware] = None
    firmware_update: typing.Optional[UserDfuStateMachine] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
