

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OnboardingStep(UniversalBaseModel):
    """
    Dictionary containing details of a single onboarding step.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the onboarding step. Valid value is `"one_time_notice"`.
    
    **Changes**: Removed type `"hotspot"` in Zulip 9.0 (feature level 259).
    
    New in Zulip 8.0 (feature level 233).
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the onboarding step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
