

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_type import MessageType
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class LobbyMessageResponse(UniversalBaseModel):
    id: SnowflakeType
    type: MessageType
    content: str
    lobby_id: SnowflakeType
    channel_id: SnowflakeType
    author: UserResponse
    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    flags: int
    application_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
