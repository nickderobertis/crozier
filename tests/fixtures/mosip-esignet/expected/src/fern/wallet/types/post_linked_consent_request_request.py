

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostLinkedConsentRequestRequest(UniversalBaseModel):
    linked_transaction_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="linkedTransactionId"),
        pydantic.Field(alias="linkedTransactionId", description="Transaction id echoed starting from /authorize call."),
    ]
    """
    Transaction id echoed starting from /authorize call.
    """

    permitted_authorize_scopes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="permittedAuthorizeScopes"),
        pydantic.Field(alias="permittedAuthorizeScopes", description="List of permitted scopes by end-user."),
    ] = None
    """
    List of permitted scopes by end-user.
    """

    accepted_claims: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="acceptedClaims"),
        pydantic.Field(
            alias="acceptedClaims", description="List of accepted essential and voluntary claims by end-user."
        ),
    ] = None
    """
    List of accepted essential and voluntary claims by end-user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
