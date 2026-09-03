

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .put_oidc_client_client_id_request_request_auth_context_refs_item import (
    PutOidcClientClientIdRequestRequestAuthContextRefsItem,
)
from .put_oidc_client_client_id_request_request_client_auth_methods_item import (
    PutOidcClientClientIdRequestRequestClientAuthMethodsItem,
)
from .put_oidc_client_client_id_request_request_grant_types_item import (
    PutOidcClientClientIdRequestRequestGrantTypesItem,
)
from .put_oidc_client_client_id_request_request_status import PutOidcClientClientIdRequestRequestStatus
from .put_oidc_client_client_id_request_request_user_claims_item import (
    PutOidcClientClientIdRequestRequestUserClaimsItem,
)


class PutOidcClientClientIdRequestRequest(UniversalBaseModel):
    client_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientName"),
        pydantic.Field(alias="clientName", description="Name of the OIDC client."),
    ]
    """
    Name of the OIDC client.
    """

    status: PutOidcClientClientIdRequestRequestStatus = pydantic.Field()
    """
    Status of OIDC client.
    """

    logo_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="logoUri"),
        pydantic.Field(
            alias="logoUri",
            description="Relying party logo URI which will used to display logo in OIDC login and consent pages.",
        ),
    ]
    """
    Relying party logo URI which will used to display logo in OIDC login and consent pages.
    """

    redirect_uris: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="redirectUris"),
        pydantic.Field(
            alias="redirectUris",
            description="Valid list of callback Uris of the relying party. When OIDC authorize API is called, any one Uri from this list should be sent as redirect_uri. authorization_code will be redirected to this Uri on successful authentication.",
        ),
    ]
    """
    Valid list of callback Uris of the relying party. When OIDC authorize API is called, any one Uri from this list should be sent as redirect_uri. authorization_code will be redirected to this Uri on successful authentication.
    """

    user_claims: typing_extensions.Annotated[
        typing.List[PutOidcClientClientIdRequestRequestUserClaimsItem],
        FieldMetadata(alias="userClaims"),
        pydantic.Field(
            alias="userClaims",
            description="Allowed user info claims, that can be requested by OIDC client in the authorize API",
        ),
    ]
    """
    Allowed user info claims, that can be requested by OIDC client in the authorize API
    """

    auth_context_refs: typing_extensions.Annotated[
        typing.List[PutOidcClientClientIdRequestRequestAuthContextRefsItem],
        FieldMetadata(alias="authContextRefs"),
        pydantic.Field(
            alias="authContextRefs",
            description="The Authentication Context Class Reference is case-sensitive string specifying a list of Authentication Context Class values that identifies the Authentication Context Class. Values that the authentication performed satisfied implying a Level Of Assurance.",
        ),
    ]
    """
    The Authentication Context Class Reference is case-sensitive string specifying a list of Authentication Context Class values that identifies the Authentication Context Class. Values that the authentication performed satisfied implying a Level Of Assurance.
    """

    grant_types: typing_extensions.Annotated[
        typing.List[PutOidcClientClientIdRequestRequestGrantTypesItem],
        FieldMetadata(alias="grantTypes"),
        pydantic.Field(alias="grantTypes", description="Form of Authorization Grant presented to token endpoint."),
    ]
    """
    Form of Authorization Grant presented to token endpoint.
    """

    client_auth_methods: typing_extensions.Annotated[
        typing.List[PutOidcClientClientIdRequestRequestClientAuthMethodsItem],
        FieldMetadata(alias="clientAuthMethods"),
        pydantic.Field(
            alias="clientAuthMethods",
            description='Auth method supported for token endpoint. At present only "private_key_jwt" is supported.',
        ),
    ]
    """
    Auth method supported for token endpoint. At present only "private_key_jwt" is supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
