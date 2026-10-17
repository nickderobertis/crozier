

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdFour(enum.StrEnum):
    AUTH_MFA_PHONE_DEFAULT = "auth_mfa_phone_default"

    def visit(self, auth_mfa_phone_default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdFour.AUTH_MFA_PHONE_DEFAULT:
            return auth_mfa_phone_default()
