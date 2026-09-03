

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostOauthClientRequestRequestAuthContextRefsItem(enum.StrEnum):
    MOSIP_IDP_ACR_STATIC_CODE = "mosip:idp:acr:static-code"
    MOSIP_IDP_ACR_GENERATED_CODE = "mosip:idp:acr:generated-code"
    MOSIP_IDP_ACR_LINKED_WALLET = "mosip:idp:acr:linked-wallet"
    MOSIP_IDP_ACR_BIOMETRICS = "mosip:idp:acr:biometrics"
    MOSIP_IDP_ACR_KNOWLEDGE = "mosip:idp:acr:knowledge"
    MOSIP_IDP_ACR_ID_TOKEN = "mosip:idp:acr:id-token"
    MOSIP_IDP_ACR_PASSWORD = "mosip:idp:acr:password"

    def visit(
        self,
        mosip_idp_acr_static_code: typing.Callable[[], T_Result],
        mosip_idp_acr_generated_code: typing.Callable[[], T_Result],
        mosip_idp_acr_linked_wallet: typing.Callable[[], T_Result],
        mosip_idp_acr_biometrics: typing.Callable[[], T_Result],
        mosip_idp_acr_knowledge: typing.Callable[[], T_Result],
        mosip_idp_acr_id_token: typing.Callable[[], T_Result],
        mosip_idp_acr_password: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_STATIC_CODE:
            return mosip_idp_acr_static_code()
        if self is PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE:
            return mosip_idp_acr_generated_code()
        if self is PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET:
            return mosip_idp_acr_linked_wallet()
        if self is PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS:
            return mosip_idp_acr_biometrics()
        if self is PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_KNOWLEDGE:
            return mosip_idp_acr_knowledge()
        if self is PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_ID_TOKEN:
            return mosip_idp_acr_id_token()
        if self is PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_PASSWORD:
            return mosip_idp_acr_password()
