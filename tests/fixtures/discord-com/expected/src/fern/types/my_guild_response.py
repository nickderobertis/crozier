

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_features import GuildFeatures
from .snowflake_type import SnowflakeType


class MyGuildResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    icon: typing.Optional[str] = None
    banner: typing.Optional[str] = None
    owner: bool
    permissions: str
    features: typing.List[GuildFeatures]
    approximate_member_count: typing.Optional[int] = None
    approximate_presence_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
