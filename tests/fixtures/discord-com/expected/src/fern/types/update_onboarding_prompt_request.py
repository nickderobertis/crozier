

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .onboarding_prompt_option_request import OnboardingPromptOptionRequest
from .onboarding_prompt_type import OnboardingPromptType
from .snowflake_type import SnowflakeType


class UpdateOnboardingPromptRequest(UniversalBaseModel):
    title: str
    options: typing.List[OnboardingPromptOptionRequest]
    single_select: typing.Optional[bool] = None
    required: typing.Optional[bool] = None
    in_onboarding: typing.Optional[bool] = None
    type: typing.Optional[OnboardingPromptType] = None
    id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
