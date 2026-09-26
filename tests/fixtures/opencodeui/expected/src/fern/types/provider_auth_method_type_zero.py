

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderAuthMethodTypeZero(enum.StrEnum):
    OAUTH = "oauth"

    def visit(self, oauth: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProviderAuthMethodTypeZero.OAUTH:
            return oauth()
