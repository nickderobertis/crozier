

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_result_outcome import AuthenticationResultOutcome
from .authentication_result_outcome_details import AuthenticationResultOutcomeDetails


class AuthenticationResult(UniversalBaseModel):
    """
    Agent-provided authentication results returned to the seller for card-based 3D Secure.
    """

    outcome: AuthenticationResultOutcome = pydantic.Field()
    """
    The outcome of this 3DS Authentication.
    """

    outcome_details: typing.Optional[AuthenticationResultOutcomeDetails] = pydantic.Field(default=None)
    """
    Detailed authentication data. This field is required when the outcome is 'authenticated', 'informational', or 'attempt_acknowledged'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
