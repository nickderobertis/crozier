

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata_flow_preference_challenge import AuthenticationMetadataFlowPreferenceChallenge
from .authentication_metadata_flow_preference_type import AuthenticationMetadataFlowPreferenceType


class AuthenticationMetadataFlowPreference(UniversalBaseModel):
    """
    Contains additional details on the seller's preference for the 3DS authentication flow. Sellers MAY request a preference, but issuers ultimately decide the actual flow.
    """

    type: AuthenticationMetadataFlowPreferenceType = pydantic.Field()
    """
    Type of flow requested for this 3DS Authentication. "challenge" requests a challenge flow; "frictionless" requests a frictionless flow.
    """

    challenge: typing.Optional[AuthenticationMetadataFlowPreferenceChallenge] = pydantic.Field(default=None)
    """
    Details about the requested challenge flow.
    """

    frictionless: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Details about the requested frictionless flow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
