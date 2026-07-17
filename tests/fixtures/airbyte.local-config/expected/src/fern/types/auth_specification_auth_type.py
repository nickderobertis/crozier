

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthSpecificationAuthType(enum.StrEnum):
    OAUTH20 = "oauth2.0"

    def visit(self, oauth20: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthSpecificationAuthType.OAUTH20:
            return oauth20()
