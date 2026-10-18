

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdFive(enum.StrEnum):
    AUTH_MFA_WEB_AUTHN_DEFAULT = "auth_mfa_web_authn_default"

    def visit(self, auth_mfa_web_authn_default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdFive.AUTH_MFA_WEB_AUTHN_DEFAULT:
            return auth_mfa_web_authn_default()
