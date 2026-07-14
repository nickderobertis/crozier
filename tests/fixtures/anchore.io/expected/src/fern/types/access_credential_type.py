

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccessCredentialType(str, enum.Enum):
    """
    The type of credential
    """

    PASSWORD = "password"

    def visit(self, password: typing.Callable[[], T_Result]) -> T_Result:
        if self is AccessCredentialType.PASSWORD:
            return password()
