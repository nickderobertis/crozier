

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationMetadataFlowPreferenceChallengeType(enum.StrEnum):
    """
    Subtype of challenge preference.
    """

    MANDATED = "mandated"
    PREFERRED = "preferred"

    def visit(self, mandated: typing.Callable[[], T_Result], preferred: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationMetadataFlowPreferenceChallengeType.MANDATED:
            return mandated()
        if self is AuthenticationMetadataFlowPreferenceChallengeType.PREFERRED:
            return preferred()
