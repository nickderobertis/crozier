

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_result_outcome import AuthenticationResultOutcome
from .authentication_result_outcome_details import AuthenticationResultOutcomeDetails


class AuthenticationResult(UniversalBaseModel):
    outcome: AuthenticationResultOutcome
    outcome_details: typing.Optional[AuthenticationResultOutcomeDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
