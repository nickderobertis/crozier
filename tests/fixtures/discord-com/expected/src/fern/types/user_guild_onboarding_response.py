

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .onboarding_prompt_response import OnboardingPromptResponse
from .snowflake_type import SnowflakeType


class UserGuildOnboardingResponse(UniversalBaseModel):
    guild_id: SnowflakeType
    prompts: typing.List[OnboardingPromptResponse]
    default_channel_ids: typing.List[SnowflakeType]
    enabled: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
