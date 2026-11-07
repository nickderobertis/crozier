

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata_flow_preference_challenge_type import AuthenticationMetadataFlowPreferenceChallengeType


class AuthenticationMetadataFlowPreferenceChallenge(UniversalBaseModel):
    """
    Details about the requested challenge flow.
    """

    type: typing.Optional[AuthenticationMetadataFlowPreferenceChallengeType] = pydantic.Field(default=None)
    """
    Subtype of challenge preference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
