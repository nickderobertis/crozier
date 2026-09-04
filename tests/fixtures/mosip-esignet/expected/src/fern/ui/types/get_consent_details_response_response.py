

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.claim_status import ClaimStatus
from .get_consent_details_response_response_consent_action import GetConsentDetailsResponseResponseConsentAction


class GetConsentDetailsResponseResponse(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transactionId"),
        pydantic.Field(
            alias="transactionId", description="This is the same transactionId sent in the oauth-details response."
        ),
    ]
    """
    This is the same transactionId sent in the oauth-details response.
    """

    consent_action: typing_extensions.Annotated[
        GetConsentDetailsResponseResponseConsentAction,
        FieldMetadata(alias="consentAction"),
        pydantic.Field(
            alias="consentAction", description="This field indicates the need to capture user consent or not"
        ),
    ]
    """
    This field indicates the need to capture user consent or not
    """

    claim_status: typing_extensions.Annotated[
        typing.List[ClaimStatus],
        FieldMetadata(alias="claimStatus"),
        pydantic.Field(
            alias="claimStatus",
            description="List of resolved claims among the requested claims with their availability and verification status.",
        ),
    ]
    """
    List of resolved claims among the requested claims with their availability and verification status.
    """

    profile_update_required: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="profileUpdateRequired"),
        pydantic.Field(
            alias="profileUpdateRequired",
            description="If true, then some or all of the essential claims are either not available or not verified. Otherwise this field is set to false",
        ),
    ]
    """
    If true, then some or all of the essential claims are either not available or not verified. Otherwise this field is set to false
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
