

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationProviderSupportedAuthenticationMethodsItem(enum.StrEnum):
    THREE_DS = "3ds"

    def visit(self, three_ds: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationProviderSupportedAuthenticationMethodsItem.THREE_DS:
            return three_ds()
