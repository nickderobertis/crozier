

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessCredentialType(enum.StrEnum):
    """
    The type of credential
    """

    PASSWORD = "password"

    def visit(self, password: typing.Callable[[], T_Result]) -> T_Result:
        if self is AccessCredentialType.PASSWORD:
            return password()
