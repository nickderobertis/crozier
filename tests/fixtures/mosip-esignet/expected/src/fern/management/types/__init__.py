



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .patch_client_client_id_request_request import PatchClientClientIdRequestRequest
    from .patch_client_client_id_request_request_additional_config import (
        PatchClientClientIdRequestRequestAdditionalConfig,
    )
    from .patch_client_client_id_request_request_additional_config_userinfo_response_type import (
        PatchClientClientIdRequestRequestAdditionalConfigUserinfoResponseType,
    )
    from .patch_client_client_id_request_request_auth_context_refs_item import (
        PatchClientClientIdRequestRequestAuthContextRefsItem,
    )
    from .patch_client_client_id_request_request_client_auth_methods_item import (
        PatchClientClientIdRequestRequestClientAuthMethodsItem,
    )
    from .patch_client_client_id_request_request_enc_public_key import PatchClientClientIdRequestRequestEncPublicKey
    from .patch_client_client_id_request_request_enc_public_key_crv import (
        PatchClientClientIdRequestRequestEncPublicKeyCrv,
    )
    from .patch_client_client_id_request_request_enc_public_key_crv_alg import (
        PatchClientClientIdRequestRequestEncPublicKeyCrvAlg,
    )
    from .patch_client_client_id_request_request_enc_public_key_crv_crv import (
        PatchClientClientIdRequestRequestEncPublicKeyCrvCrv,
    )
    from .patch_client_client_id_request_request_enc_public_key_crv_kty import (
        PatchClientClientIdRequestRequestEncPublicKeyCrvKty,
    )
    from .patch_client_client_id_request_request_enc_public_key_crv_use import (
        PatchClientClientIdRequestRequestEncPublicKeyCrvUse,
    )
    from .patch_client_client_id_request_request_enc_public_key_e import PatchClientClientIdRequestRequestEncPublicKeyE
    from .patch_client_client_id_request_request_enc_public_key_e_alg import (
        PatchClientClientIdRequestRequestEncPublicKeyEAlg,
    )
    from .patch_client_client_id_request_request_enc_public_key_e_kty import (
        PatchClientClientIdRequestRequestEncPublicKeyEKty,
    )
    from .patch_client_client_id_request_request_enc_public_key_e_use import (
        PatchClientClientIdRequestRequestEncPublicKeyEUse,
    )
    from .patch_client_client_id_request_request_enc_public_key_ee import (
        PatchClientClientIdRequestRequestEncPublicKeyEe,
    )
    from .patch_client_client_id_request_request_grant_types_item import PatchClientClientIdRequestRequestGrantTypesItem
    from .patch_client_client_id_request_request_status import PatchClientClientIdRequestRequestStatus
    from .patch_client_client_id_request_request_user_claims_item import PatchClientClientIdRequestRequestUserClaimsItem
    from .patch_client_client_id_response import PatchClientClientIdResponse
    from .patch_client_client_id_response_errors_item import PatchClientClientIdResponseErrorsItem
    from .patch_client_client_id_response_errors_item_error_code import PatchClientClientIdResponseErrorsItemErrorCode
    from .patch_client_client_id_response_response import PatchClientClientIdResponseResponse
    from .patch_client_client_id_response_response_status import PatchClientClientIdResponseResponseStatus
    from .post_client_mgmt_client_request_request import PostClientMgmtClientRequestRequest
    from .post_client_mgmt_client_request_request_additional_config import (
        PostClientMgmtClientRequestRequestAdditionalConfig,
    )
    from .post_client_mgmt_client_request_request_additional_config_userinfo_response_type import (
        PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType,
    )
    from .post_client_mgmt_client_request_request_auth_context_refs_item import (
        PostClientMgmtClientRequestRequestAuthContextRefsItem,
    )
    from .post_client_mgmt_client_request_request_client_auth_methods_item import (
        PostClientMgmtClientRequestRequestClientAuthMethodsItem,
    )
    from .post_client_mgmt_client_request_request_grant_types_item import (
        PostClientMgmtClientRequestRequestGrantTypesItem,
    )
    from .post_client_mgmt_client_request_request_user_claims_item import (
        PostClientMgmtClientRequestRequestUserClaimsItem,
    )
    from .post_client_mgmt_client_response import PostClientMgmtClientResponse
    from .post_client_mgmt_client_response_errors_item import PostClientMgmtClientResponseErrorsItem
    from .post_client_mgmt_client_response_errors_item_error_code import PostClientMgmtClientResponseErrorsItemErrorCode
    from .post_client_mgmt_client_response_response import PostClientMgmtClientResponseResponse
    from .post_client_mgmt_client_response_response_status import PostClientMgmtClientResponseResponseStatus
    from .post_client_request_request import PostClientRequestRequest
    from .post_client_request_request_auth_context_refs_item import PostClientRequestRequestAuthContextRefsItem
    from .post_client_request_request_client_auth_methods_item import PostClientRequestRequestClientAuthMethodsItem
    from .post_client_request_request_grant_types_item import PostClientRequestRequestGrantTypesItem
    from .post_client_request_request_user_claims_item import PostClientRequestRequestUserClaimsItem
    from .post_client_response import PostClientResponse
    from .post_client_response_errors_item import PostClientResponseErrorsItem
    from .post_client_response_errors_item_error_code import PostClientResponseErrorsItemErrorCode
    from .post_client_response_response import PostClientResponseResponse
    from .post_client_response_response_status import PostClientResponseResponseStatus
    from .post_oauth_client_request_request import PostOauthClientRequestRequest
    from .post_oauth_client_request_request_auth_context_refs_item import (
        PostOauthClientRequestRequestAuthContextRefsItem,
    )
    from .post_oauth_client_request_request_client_auth_methods_item import (
        PostOauthClientRequestRequestClientAuthMethodsItem,
    )
    from .post_oauth_client_request_request_grant_types_item import PostOauthClientRequestRequestGrantTypesItem
    from .post_oauth_client_request_request_user_claims_item import PostOauthClientRequestRequestUserClaimsItem
    from .post_oauth_client_response import PostOauthClientResponse
    from .post_oauth_client_response_errors_item import PostOauthClientResponseErrorsItem
    from .post_oauth_client_response_errors_item_error_code import PostOauthClientResponseErrorsItemErrorCode
    from .post_oauth_client_response_response import PostOauthClientResponseResponse
    from .post_oauth_client_response_response_status import PostOauthClientResponseResponseStatus
    from .put_client_client_id_request_request import PutClientClientIdRequestRequest
    from .put_client_client_id_request_request_additional_config import PutClientClientIdRequestRequestAdditionalConfig
    from .put_client_client_id_request_request_additional_config_userinfo_response_type import (
        PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType,
    )
    from .put_client_client_id_request_request_auth_context_refs_item import (
        PutClientClientIdRequestRequestAuthContextRefsItem,
    )
    from .put_client_client_id_request_request_client_auth_methods_item import (
        PutClientClientIdRequestRequestClientAuthMethodsItem,
    )
    from .put_client_client_id_request_request_grant_types_item import PutClientClientIdRequestRequestGrantTypesItem
    from .put_client_client_id_request_request_status import PutClientClientIdRequestRequestStatus
    from .put_client_client_id_request_request_user_claims_item import PutClientClientIdRequestRequestUserClaimsItem
    from .put_client_client_id_response import PutClientClientIdResponse
    from .put_client_client_id_response_errors_item import PutClientClientIdResponseErrorsItem
    from .put_client_client_id_response_errors_item_error_code import PutClientClientIdResponseErrorsItemErrorCode
    from .put_client_client_id_response_response import PutClientClientIdResponseResponse
    from .put_client_client_id_response_response_status import PutClientClientIdResponseResponseStatus
    from .put_oauth_client_client_id_request_request import PutOauthClientClientIdRequestRequest
    from .put_oauth_client_client_id_request_request_auth_context_refs_item import (
        PutOauthClientClientIdRequestRequestAuthContextRefsItem,
    )
    from .put_oauth_client_client_id_request_request_client_auth_methods_item import (
        PutOauthClientClientIdRequestRequestClientAuthMethodsItem,
    )
    from .put_oauth_client_client_id_request_request_grant_types_item import (
        PutOauthClientClientIdRequestRequestGrantTypesItem,
    )
    from .put_oauth_client_client_id_request_request_status import PutOauthClientClientIdRequestRequestStatus
    from .put_oauth_client_client_id_request_request_user_claims_item import (
        PutOauthClientClientIdRequestRequestUserClaimsItem,
    )
    from .put_oauth_client_client_id_response import PutOauthClientClientIdResponse
    from .put_oauth_client_client_id_response_errors_item import PutOauthClientClientIdResponseErrorsItem
    from .put_oauth_client_client_id_response_errors_item_error_code import (
        PutOauthClientClientIdResponseErrorsItemErrorCode,
    )
    from .put_oauth_client_client_id_response_response import PutOauthClientClientIdResponseResponse
    from .put_oauth_client_client_id_response_response_status import PutOauthClientClientIdResponseResponseStatus
    from .put_oidc_client_client_id_request_request import PutOidcClientClientIdRequestRequest
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
    from .put_oidc_client_client_id_response import PutOidcClientClientIdResponse
    from .put_oidc_client_client_id_response_errors_item import PutOidcClientClientIdResponseErrorsItem
    from .put_oidc_client_client_id_response_errors_item_error_code import (
        PutOidcClientClientIdResponseErrorsItemErrorCode,
    )
    from .put_oidc_client_client_id_response_response import PutOidcClientClientIdResponseResponse
    from .put_oidc_client_client_id_response_response_status import PutOidcClientClientIdResponseResponseStatus
_dynamic_imports: typing.Dict[str, str] = {
    "PatchClientClientIdRequestRequest": ".patch_client_client_id_request_request",
    "PatchClientClientIdRequestRequestAdditionalConfig": ".patch_client_client_id_request_request_additional_config",
    "PatchClientClientIdRequestRequestAdditionalConfigUserinfoResponseType": ".patch_client_client_id_request_request_additional_config_userinfo_response_type",
    "PatchClientClientIdRequestRequestAuthContextRefsItem": ".patch_client_client_id_request_request_auth_context_refs_item",
    "PatchClientClientIdRequestRequestClientAuthMethodsItem": ".patch_client_client_id_request_request_client_auth_methods_item",
    "PatchClientClientIdRequestRequestEncPublicKey": ".patch_client_client_id_request_request_enc_public_key",
    "PatchClientClientIdRequestRequestEncPublicKeyCrv": ".patch_client_client_id_request_request_enc_public_key_crv",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvAlg": ".patch_client_client_id_request_request_enc_public_key_crv_alg",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvCrv": ".patch_client_client_id_request_request_enc_public_key_crv_crv",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvKty": ".patch_client_client_id_request_request_enc_public_key_crv_kty",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvUse": ".patch_client_client_id_request_request_enc_public_key_crv_use",
    "PatchClientClientIdRequestRequestEncPublicKeyE": ".patch_client_client_id_request_request_enc_public_key_e",
    "PatchClientClientIdRequestRequestEncPublicKeyEAlg": ".patch_client_client_id_request_request_enc_public_key_e_alg",
    "PatchClientClientIdRequestRequestEncPublicKeyEKty": ".patch_client_client_id_request_request_enc_public_key_e_kty",
    "PatchClientClientIdRequestRequestEncPublicKeyEUse": ".patch_client_client_id_request_request_enc_public_key_e_use",
    "PatchClientClientIdRequestRequestEncPublicKeyEe": ".patch_client_client_id_request_request_enc_public_key_ee",
    "PatchClientClientIdRequestRequestGrantTypesItem": ".patch_client_client_id_request_request_grant_types_item",
    "PatchClientClientIdRequestRequestStatus": ".patch_client_client_id_request_request_status",
    "PatchClientClientIdRequestRequestUserClaimsItem": ".patch_client_client_id_request_request_user_claims_item",
    "PatchClientClientIdResponse": ".patch_client_client_id_response",
    "PatchClientClientIdResponseErrorsItem": ".patch_client_client_id_response_errors_item",
    "PatchClientClientIdResponseErrorsItemErrorCode": ".patch_client_client_id_response_errors_item_error_code",
    "PatchClientClientIdResponseResponse": ".patch_client_client_id_response_response",
    "PatchClientClientIdResponseResponseStatus": ".patch_client_client_id_response_response_status",
    "PostClientMgmtClientRequestRequest": ".post_client_mgmt_client_request_request",
    "PostClientMgmtClientRequestRequestAdditionalConfig": ".post_client_mgmt_client_request_request_additional_config",
    "PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType": ".post_client_mgmt_client_request_request_additional_config_userinfo_response_type",
    "PostClientMgmtClientRequestRequestAuthContextRefsItem": ".post_client_mgmt_client_request_request_auth_context_refs_item",
    "PostClientMgmtClientRequestRequestClientAuthMethodsItem": ".post_client_mgmt_client_request_request_client_auth_methods_item",
    "PostClientMgmtClientRequestRequestGrantTypesItem": ".post_client_mgmt_client_request_request_grant_types_item",
    "PostClientMgmtClientRequestRequestUserClaimsItem": ".post_client_mgmt_client_request_request_user_claims_item",
    "PostClientMgmtClientResponse": ".post_client_mgmt_client_response",
    "PostClientMgmtClientResponseErrorsItem": ".post_client_mgmt_client_response_errors_item",
    "PostClientMgmtClientResponseErrorsItemErrorCode": ".post_client_mgmt_client_response_errors_item_error_code",
    "PostClientMgmtClientResponseResponse": ".post_client_mgmt_client_response_response",
    "PostClientMgmtClientResponseResponseStatus": ".post_client_mgmt_client_response_response_status",
    "PostClientRequestRequest": ".post_client_request_request",
    "PostClientRequestRequestAuthContextRefsItem": ".post_client_request_request_auth_context_refs_item",
    "PostClientRequestRequestClientAuthMethodsItem": ".post_client_request_request_client_auth_methods_item",
    "PostClientRequestRequestGrantTypesItem": ".post_client_request_request_grant_types_item",
    "PostClientRequestRequestUserClaimsItem": ".post_client_request_request_user_claims_item",
    "PostClientResponse": ".post_client_response",
    "PostClientResponseErrorsItem": ".post_client_response_errors_item",
    "PostClientResponseErrorsItemErrorCode": ".post_client_response_errors_item_error_code",
    "PostClientResponseResponse": ".post_client_response_response",
    "PostClientResponseResponseStatus": ".post_client_response_response_status",
    "PostOauthClientRequestRequest": ".post_oauth_client_request_request",
    "PostOauthClientRequestRequestAuthContextRefsItem": ".post_oauth_client_request_request_auth_context_refs_item",
    "PostOauthClientRequestRequestClientAuthMethodsItem": ".post_oauth_client_request_request_client_auth_methods_item",
    "PostOauthClientRequestRequestGrantTypesItem": ".post_oauth_client_request_request_grant_types_item",
    "PostOauthClientRequestRequestUserClaimsItem": ".post_oauth_client_request_request_user_claims_item",
    "PostOauthClientResponse": ".post_oauth_client_response",
    "PostOauthClientResponseErrorsItem": ".post_oauth_client_response_errors_item",
    "PostOauthClientResponseErrorsItemErrorCode": ".post_oauth_client_response_errors_item_error_code",
    "PostOauthClientResponseResponse": ".post_oauth_client_response_response",
    "PostOauthClientResponseResponseStatus": ".post_oauth_client_response_response_status",
    "PutClientClientIdRequestRequest": ".put_client_client_id_request_request",
    "PutClientClientIdRequestRequestAdditionalConfig": ".put_client_client_id_request_request_additional_config",
    "PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType": ".put_client_client_id_request_request_additional_config_userinfo_response_type",
    "PutClientClientIdRequestRequestAuthContextRefsItem": ".put_client_client_id_request_request_auth_context_refs_item",
    "PutClientClientIdRequestRequestClientAuthMethodsItem": ".put_client_client_id_request_request_client_auth_methods_item",
    "PutClientClientIdRequestRequestGrantTypesItem": ".put_client_client_id_request_request_grant_types_item",
    "PutClientClientIdRequestRequestStatus": ".put_client_client_id_request_request_status",
    "PutClientClientIdRequestRequestUserClaimsItem": ".put_client_client_id_request_request_user_claims_item",
    "PutClientClientIdResponse": ".put_client_client_id_response",
    "PutClientClientIdResponseErrorsItem": ".put_client_client_id_response_errors_item",
    "PutClientClientIdResponseErrorsItemErrorCode": ".put_client_client_id_response_errors_item_error_code",
    "PutClientClientIdResponseResponse": ".put_client_client_id_response_response",
    "PutClientClientIdResponseResponseStatus": ".put_client_client_id_response_response_status",
    "PutOauthClientClientIdRequestRequest": ".put_oauth_client_client_id_request_request",
    "PutOauthClientClientIdRequestRequestAuthContextRefsItem": ".put_oauth_client_client_id_request_request_auth_context_refs_item",
    "PutOauthClientClientIdRequestRequestClientAuthMethodsItem": ".put_oauth_client_client_id_request_request_client_auth_methods_item",
    "PutOauthClientClientIdRequestRequestGrantTypesItem": ".put_oauth_client_client_id_request_request_grant_types_item",
    "PutOauthClientClientIdRequestRequestStatus": ".put_oauth_client_client_id_request_request_status",
    "PutOauthClientClientIdRequestRequestUserClaimsItem": ".put_oauth_client_client_id_request_request_user_claims_item",
    "PutOauthClientClientIdResponse": ".put_oauth_client_client_id_response",
    "PutOauthClientClientIdResponseErrorsItem": ".put_oauth_client_client_id_response_errors_item",
    "PutOauthClientClientIdResponseErrorsItemErrorCode": ".put_oauth_client_client_id_response_errors_item_error_code",
    "PutOauthClientClientIdResponseResponse": ".put_oauth_client_client_id_response_response",
    "PutOauthClientClientIdResponseResponseStatus": ".put_oauth_client_client_id_response_response_status",
    "PutOidcClientClientIdRequestRequest": ".put_oidc_client_client_id_request_request",
    "PutOidcClientClientIdRequestRequestAuthContextRefsItem": ".put_oidc_client_client_id_request_request_auth_context_refs_item",
    "PutOidcClientClientIdRequestRequestClientAuthMethodsItem": ".put_oidc_client_client_id_request_request_client_auth_methods_item",
    "PutOidcClientClientIdRequestRequestGrantTypesItem": ".put_oidc_client_client_id_request_request_grant_types_item",
    "PutOidcClientClientIdRequestRequestStatus": ".put_oidc_client_client_id_request_request_status",
    "PutOidcClientClientIdRequestRequestUserClaimsItem": ".put_oidc_client_client_id_request_request_user_claims_item",
    "PutOidcClientClientIdResponse": ".put_oidc_client_client_id_response",
    "PutOidcClientClientIdResponseErrorsItem": ".put_oidc_client_client_id_response_errors_item",
    "PutOidcClientClientIdResponseErrorsItemErrorCode": ".put_oidc_client_client_id_response_errors_item_error_code",
    "PutOidcClientClientIdResponseResponse": ".put_oidc_client_client_id_response_response",
    "PutOidcClientClientIdResponseResponseStatus": ".put_oidc_client_client_id_response_response_status",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "PatchClientClientIdRequestRequest",
    "PatchClientClientIdRequestRequestAdditionalConfig",
    "PatchClientClientIdRequestRequestAdditionalConfigUserinfoResponseType",
    "PatchClientClientIdRequestRequestAuthContextRefsItem",
    "PatchClientClientIdRequestRequestClientAuthMethodsItem",
    "PatchClientClientIdRequestRequestEncPublicKey",
    "PatchClientClientIdRequestRequestEncPublicKeyCrv",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvAlg",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvCrv",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvKty",
    "PatchClientClientIdRequestRequestEncPublicKeyCrvUse",
    "PatchClientClientIdRequestRequestEncPublicKeyE",
    "PatchClientClientIdRequestRequestEncPublicKeyEAlg",
    "PatchClientClientIdRequestRequestEncPublicKeyEKty",
    "PatchClientClientIdRequestRequestEncPublicKeyEUse",
    "PatchClientClientIdRequestRequestEncPublicKeyEe",
    "PatchClientClientIdRequestRequestGrantTypesItem",
    "PatchClientClientIdRequestRequestStatus",
    "PatchClientClientIdRequestRequestUserClaimsItem",
    "PatchClientClientIdResponse",
    "PatchClientClientIdResponseErrorsItem",
    "PatchClientClientIdResponseErrorsItemErrorCode",
    "PatchClientClientIdResponseResponse",
    "PatchClientClientIdResponseResponseStatus",
    "PostClientMgmtClientRequestRequest",
    "PostClientMgmtClientRequestRequestAdditionalConfig",
    "PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType",
    "PostClientMgmtClientRequestRequestAuthContextRefsItem",
    "PostClientMgmtClientRequestRequestClientAuthMethodsItem",
    "PostClientMgmtClientRequestRequestGrantTypesItem",
    "PostClientMgmtClientRequestRequestUserClaimsItem",
    "PostClientMgmtClientResponse",
    "PostClientMgmtClientResponseErrorsItem",
    "PostClientMgmtClientResponseErrorsItemErrorCode",
    "PostClientMgmtClientResponseResponse",
    "PostClientMgmtClientResponseResponseStatus",
    "PostClientRequestRequest",
    "PostClientRequestRequestAuthContextRefsItem",
    "PostClientRequestRequestClientAuthMethodsItem",
    "PostClientRequestRequestGrantTypesItem",
    "PostClientRequestRequestUserClaimsItem",
    "PostClientResponse",
    "PostClientResponseErrorsItem",
    "PostClientResponseErrorsItemErrorCode",
    "PostClientResponseResponse",
    "PostClientResponseResponseStatus",
    "PostOauthClientRequestRequest",
    "PostOauthClientRequestRequestAuthContextRefsItem",
    "PostOauthClientRequestRequestClientAuthMethodsItem",
    "PostOauthClientRequestRequestGrantTypesItem",
    "PostOauthClientRequestRequestUserClaimsItem",
    "PostOauthClientResponse",
    "PostOauthClientResponseErrorsItem",
    "PostOauthClientResponseErrorsItemErrorCode",
    "PostOauthClientResponseResponse",
    "PostOauthClientResponseResponseStatus",
    "PutClientClientIdRequestRequest",
    "PutClientClientIdRequestRequestAdditionalConfig",
    "PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType",
    "PutClientClientIdRequestRequestAuthContextRefsItem",
    "PutClientClientIdRequestRequestClientAuthMethodsItem",
    "PutClientClientIdRequestRequestGrantTypesItem",
    "PutClientClientIdRequestRequestStatus",
    "PutClientClientIdRequestRequestUserClaimsItem",
    "PutClientClientIdResponse",
    "PutClientClientIdResponseErrorsItem",
    "PutClientClientIdResponseErrorsItemErrorCode",
    "PutClientClientIdResponseResponse",
    "PutClientClientIdResponseResponseStatus",
    "PutOauthClientClientIdRequestRequest",
    "PutOauthClientClientIdRequestRequestAuthContextRefsItem",
    "PutOauthClientClientIdRequestRequestClientAuthMethodsItem",
    "PutOauthClientClientIdRequestRequestGrantTypesItem",
    "PutOauthClientClientIdRequestRequestStatus",
    "PutOauthClientClientIdRequestRequestUserClaimsItem",
    "PutOauthClientClientIdResponse",
    "PutOauthClientClientIdResponseErrorsItem",
    "PutOauthClientClientIdResponseErrorsItemErrorCode",
    "PutOauthClientClientIdResponseResponse",
    "PutOauthClientClientIdResponseResponseStatus",
    "PutOidcClientClientIdRequestRequest",
    "PutOidcClientClientIdRequestRequestAuthContextRefsItem",
    "PutOidcClientClientIdRequestRequestClientAuthMethodsItem",
    "PutOidcClientClientIdRequestRequestGrantTypesItem",
    "PutOidcClientClientIdRequestRequestStatus",
    "PutOidcClientClientIdRequestRequestUserClaimsItem",
    "PutOidcClientClientIdResponse",
    "PutOidcClientClientIdResponseErrorsItem",
    "PutOidcClientClientIdResponseErrorsItemErrorCode",
    "PutOidcClientClientIdResponseResponse",
    "PutOidcClientClientIdResponseResponseStatus",
]
