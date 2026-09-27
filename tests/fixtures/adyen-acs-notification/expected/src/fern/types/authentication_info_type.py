

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInfoType(enum.StrEnum):
    """
    The type of authentication performed. Possible values:

    * **frictionless**
    * **challenge**
    """

    FRICTIONLESS = "frictionless"
    CHALLENGE = "challenge"

    def visit(self, frictionless: typing.Callable[[], T_Result], challenge: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationInfoType.FRICTIONLESS:
            return frictionless()
        if self is AuthenticationInfoType.CHALLENGE:
            return challenge()
