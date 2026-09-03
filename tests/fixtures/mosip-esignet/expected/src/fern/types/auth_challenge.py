

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auth_challenge_auth_factor_type import AuthChallengeAuthFactorType
from .auth_challenge_format import AuthChallengeFormat


class AuthChallenge(UniversalBaseModel):
    """
    Model to take any type of challenge from the end user as part of authenticate request.
    """

    auth_factor_type: typing_extensions.Annotated[
        AuthChallengeAuthFactorType,
        FieldMetadata(alias="authFactorType"),
        pydantic.Field(
            alias="authFactorType",
            description="Defines the type of auth challenge. It should be same as authfactor.type (oauth-details response).",
        ),
    ]
    """
    Defines the type of auth challenge. It should be same as authfactor.type (oauth-details response).
    """

    challenge: str = pydantic.Field()
    """
    Actual challenge as string.
    """

    format: AuthChallengeFormat = pydantic.Field()
    """
    Format of the challenge provided.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
