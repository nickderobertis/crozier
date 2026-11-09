

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MultiPartyAuthorizeRequestAuthorizationOperation(enum.StrEnum):
    REVOKE_AGENT = "revoke_agent"
    ROTATE_ORG_KEY = "rotate_org_key"
    CHANGE_JURISDICTION = "change_jurisdiction"
    MODIFY_RECOVERY_CONFIG = "modify_recovery_config"

    def visit(
        self,
        revoke_agent: typing.Callable[[], T_Result],
        rotate_org_key: typing.Callable[[], T_Result],
        change_jurisdiction: typing.Callable[[], T_Result],
        modify_recovery_config: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MultiPartyAuthorizeRequestAuthorizationOperation.REVOKE_AGENT:
            return revoke_agent()
        if self is MultiPartyAuthorizeRequestAuthorizationOperation.ROTATE_ORG_KEY:
            return rotate_org_key()
        if self is MultiPartyAuthorizeRequestAuthorizationOperation.CHANGE_JURISDICTION:
            return change_jurisdiction()
        if self is MultiPartyAuthorizeRequestAuthorizationOperation.MODIFY_RECOVERY_CONFIG:
            return modify_recovery_config()
