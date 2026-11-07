

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_status_clear_at_time import UserStatusClearAtTime
from .user_status_clear_at_type import UserStatusClearAtType


class UserStatusClearAt(UniversalBaseModel):
    type: UserStatusClearAtType
    time: UserStatusClearAtTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
