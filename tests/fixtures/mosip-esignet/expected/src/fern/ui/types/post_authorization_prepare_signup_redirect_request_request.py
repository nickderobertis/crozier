

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAuthorizationPrepareSignupRedirectRequestRequest(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="Authenticated OIDC transaction ID."),
    ]
    """
    Authenticated OIDC transaction ID.
    """

    path_fragment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pathFragment"),
        pydantic.Field(
            alias="pathFragment",
            description="Path fragment to resume back the OIDC flow after completing the KYC process in signup portal.",
        ),
    ]
    """
    Path fragment to resume back the OIDC flow after completing the KYC process in signup portal.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
