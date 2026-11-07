

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upload_metadata import UploadMetadata
from .user_dfu_state_machine_status import UserDfuStateMachineStatus


class UserDfuStateMachine(UniversalBaseModel):
    created: typing.Optional[dt.datetime] = None
    from_version: typing.Optional[str] = None
    metadata: typing.Optional[UploadMetadata] = None
    status: typing.Optional[UserDfuStateMachineStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
