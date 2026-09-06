

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class EmojiResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    user: typing.Optional[UserResponse] = None
    roles: typing.List[SnowflakeType]
    require_colons: bool
    managed: bool
    animated: bool
    available: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
