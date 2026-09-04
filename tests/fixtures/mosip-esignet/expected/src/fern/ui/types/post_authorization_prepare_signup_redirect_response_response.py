

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAuthorizationPrepareSignupRedirectResponseResponse(UniversalBaseModel):
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

    id_token: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="idToken"),
        pydantic.Field(alias="idToken", description="This field holds the ID token generated for signup service"),
    ]
    """
    This field holds the ID token generated for signup service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
