

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .patch_client_client_id_request_request_additional_config import PatchClientClientIdRequestRequestAdditionalConfig
from .patch_client_client_id_request_request_auth_context_refs_item import (
    PatchClientClientIdRequestRequestAuthContextRefsItem,
)
from .patch_client_client_id_request_request_client_auth_methods_item import (
    PatchClientClientIdRequestRequestClientAuthMethodsItem,
)
from .patch_client_client_id_request_request_enc_public_key import PatchClientClientIdRequestRequestEncPublicKey
from .patch_client_client_id_request_request_grant_types_item import PatchClientClientIdRequestRequestGrantTypesItem
from .patch_client_client_id_request_request_status import PatchClientClientIdRequestRequestStatus
from .patch_client_client_id_request_request_user_claims_item import PatchClientClientIdRequestRequestUserClaimsItem


class PatchClientClientIdRequestRequest(UniversalBaseModel):
    """
    All fields are optional. Only provided fields will be updated.
    """

    client_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientName"),
        pydantic.Field(alias="clientName", description="Name of the OAuth/OIDC client."),
    ] = None
    """
    Name of the OAuth/OIDC client.
    """

    client_name_lang_map: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="clientNameLangMap"),
        pydantic.Field(alias="clientNameLangMap", description="Client name in different languages."),
    ] = None
    """
    Client name in different languages.
    """

    status: typing.Optional[PatchClientClientIdRequestRequestStatus] = pydantic.Field(default=None)
    """
    Status of the Client.
    """

    logo_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoUri"),
        pydantic.Field(alias="logoUri", description="Relying party logo URI."),
    ] = None
    """
    Relying party logo URI.
    """

    redirect_uris: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="redirectUris"),
        pydantic.Field(alias="redirectUris", description="Valid list of callback URIs."),
    ] = None
    """
    Valid list of callback URIs.
    """

    user_claims: typing_extensions.Annotated[
        typing.Optional[typing.List[PatchClientClientIdRequestRequestUserClaimsItem]],
        FieldMetadata(alias="userClaims"),
        pydantic.Field(
            alias="userClaims", description="Allowed user info claims that can be requested by OIDC client."
        ),
    ] = None
    """
    Allowed user info claims that can be requested by OIDC client.
    """

    auth_context_refs: typing_extensions.Annotated[
        typing.Optional[typing.List[PatchClientClientIdRequestRequestAuthContextRefsItem]],
        FieldMetadata(alias="authContextRefs"),
        pydantic.Field(alias="authContextRefs", description="Authentication Context Class Reference values."),
    ] = None
    """
    Authentication Context Class Reference values.
    """

    grant_types: typing_extensions.Annotated[
        typing.Optional[typing.List[PatchClientClientIdRequestRequestGrantTypesItem]],
        FieldMetadata(alias="grantTypes"),
        pydantic.Field(alias="grantTypes", description="Form of Authorization Grant presented to token endpoint."),
    ] = None
    """
    Form of Authorization Grant presented to token endpoint.
    """

    client_auth_methods: typing_extensions.Annotated[
        typing.Optional[typing.List[PatchClientClientIdRequestRequestClientAuthMethodsItem]],
        FieldMetadata(alias="clientAuthMethods"),
        pydantic.Field(
            alias="clientAuthMethods",
            description='Auth method supported for token endpoint. At present only "private_key_jwt" is supported.',
        ),
    ] = None
    """
    Auth method supported for token endpoint. At present only "private_key_jwt" is supported.
    """

    additional_config: typing_extensions.Annotated[
        typing.Optional[PatchClientClientIdRequestRequestAdditionalConfig],
        FieldMetadata(alias="additionalConfig"),
        pydantic.Field(
            alias="additionalConfig",
            description="This parameter allow us to configure the required values based on their specific authentication and integration needs, ensuring efficient implementation of eSignet for ID verification/authentication.",
        ),
    ] = None
    """
    This parameter allow us to configure the required values based on their specific authentication and integration needs, ensuring efficient implementation of eSignet for ID verification/authentication.
    """

    enc_public_key: typing_extensions.Annotated[
        typing.Optional[PatchClientClientIdRequestRequestEncPublicKey],
        FieldMetadata(alias="encPublicKey"),
        pydantic.Field(
            alias="encPublicKey",
            description="Encryption public key in JWK format for userinfo JWE encryption.\n- Set to a valid JWK object to update\n- Set to null to clear the encryption key\n- Omit to leave unchanged",
        ),
    ] = None
    """
    Encryption public key in JWK format for userinfo JWE encryption.
    - Set to a valid JWK object to update
    - Set to null to clear the encryption key
    - Omit to leave unchanged
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
