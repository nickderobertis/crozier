

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationMetadataFlowPreferenceType(enum.StrEnum):
    """
    Type of flow requested for this 3DS Authentication. "challenge" requests a challenge flow; "frictionless" requests a frictionless flow.
    """

    CHALLENGE = "challenge"
    FRICTIONLESS = "frictionless"

    def visit(self, challenge: typing.Callable[[], T_Result], frictionless: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationMetadataFlowPreferenceType.CHALLENGE:
            return challenge()
        if self is AuthenticationMetadataFlowPreferenceType.FRICTIONLESS:
            return frictionless()
