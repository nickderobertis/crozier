

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_authenticate_v3response_response_consent_action import PostAuthenticateV3ResponseResponseConsentAction


class PostAuthenticateV3ResponseResponse(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionId"),
        pydantic.Field(
            alias="transactionId", description="This is the same transactionId sent in the oauth-details response."
        ),
    ] = None
    """
    This is the same transactionId sent in the oauth-details response.
    """

    consent_action: typing_extensions.Annotated[
        typing.Optional[PostAuthenticateV3ResponseResponseConsentAction],
        FieldMetadata(alias="consentAction"),
        pydantic.Field(
            alias="consentAction", description="This field indicates the need to capture user consent or not"
        ),
    ] = None
    """
    This field indicates the need to capture user consent or not
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
