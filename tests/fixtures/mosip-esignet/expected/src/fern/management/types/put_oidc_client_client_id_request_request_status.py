

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutOidcClientClientIdRequestRequestStatus(enum.StrEnum):
    """
    Status of OIDC client.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutOidcClientClientIdRequestRequestStatus.ACTIVE:
            return active()
        if self is PutOidcClientClientIdRequestRequestStatus.INACTIVE:
            return inactive()
