

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AuthSpecificationAuthType(str, enum.Enum):
    OAUTH20 = "oauth2.0"

    def visit(self, oauth20: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthSpecificationAuthType.OAUTH20:
            return oauth20()
