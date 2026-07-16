

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteUserCredentialRequestCredentialType(enum.StrEnum):
    PASSWORD = "password"

    def visit(self, password: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteUserCredentialRequestCredentialType.PASSWORD:
            return password()
