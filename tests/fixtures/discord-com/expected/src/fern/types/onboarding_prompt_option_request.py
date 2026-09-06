

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType


class OnboardingPromptOptionRequest(UniversalBaseModel):
    id: typing.Optional[SnowflakeType] = None
    title: str
    description: typing.Optional[str] = None
    emoji_id: typing.Optional[SnowflakeType] = None
    emoji_name: typing.Optional[str] = None
    emoji_animated: typing.Optional[bool] = None
    role_ids: typing.Optional[typing.List[SnowflakeType]] = None
    channel_ids: typing.Optional[typing.List[SnowflakeType]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
