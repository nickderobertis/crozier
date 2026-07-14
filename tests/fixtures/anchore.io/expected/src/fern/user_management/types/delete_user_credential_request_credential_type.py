

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeleteUserCredentialRequestCredentialType(str, enum.Enum):
    PASSWORD = "password"

    def visit(self, password: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteUserCredentialRequestCredentialType.PASSWORD:
            return password()
