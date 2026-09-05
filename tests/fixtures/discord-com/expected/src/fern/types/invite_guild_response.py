

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_features import GuildFeatures
from .guild_nsfw_content_level import GuildNsfwContentLevel
from .snowflake_type import SnowflakeType
from .verification_levels import VerificationLevels


class InviteGuildResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    splash: typing.Optional[str] = None
    banner: typing.Optional[str] = None
    description: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    features: typing.List[GuildFeatures]
    verification_level: typing.Optional[VerificationLevels] = None
    vanity_url_code: typing.Optional[str] = None
    nsfw_level: typing.Optional[GuildNsfwContentLevel] = None
    nsfw: typing.Optional[bool] = None
    premium_subscription_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
