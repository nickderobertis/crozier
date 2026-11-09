

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationMetadataFlowPreferenceType(enum.StrEnum):
    CHALLENGE = "challenge"
    FRICTIONLESS = "frictionless"

    def visit(self, challenge: typing.Callable[[], T_Result], frictionless: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationMetadataFlowPreferenceType.CHALLENGE:
            return challenge()
        if self is AuthenticationMetadataFlowPreferenceType.FRICTIONLESS:
            return frictionless()
