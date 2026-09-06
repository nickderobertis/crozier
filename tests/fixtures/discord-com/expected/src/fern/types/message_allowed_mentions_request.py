

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .allowed_mention_types import AllowedMentionTypes
from .snowflake_type import SnowflakeType


class MessageAllowedMentionsRequest(UniversalBaseModel):
    parse: typing.Optional[typing.List[typing.Optional[AllowedMentionTypes]]] = None
    users: typing.Optional[typing.List[typing.Optional[SnowflakeType]]] = None
    roles: typing.Optional[typing.List[typing.Optional[SnowflakeType]]] = None
    replied_user: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
