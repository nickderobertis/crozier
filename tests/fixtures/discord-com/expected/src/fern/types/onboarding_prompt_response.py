

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .onboarding_prompt_option_response import OnboardingPromptOptionResponse
from .onboarding_prompt_type import OnboardingPromptType
from .snowflake_type import SnowflakeType


class OnboardingPromptResponse(UniversalBaseModel):
    id: SnowflakeType
    title: str
    options: typing.List[OnboardingPromptOptionResponse]
    single_select: bool
    required: bool
    in_onboarding: bool
    type: OnboardingPromptType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
