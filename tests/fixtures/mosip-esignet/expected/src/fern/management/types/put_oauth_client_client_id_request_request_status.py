

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutOauthClientClientIdRequestRequestStatus(enum.StrEnum):
    """
    Status of the Client.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutOauthClientClientIdRequestRequestStatus.ACTIVE:
            return active()
        if self is PutOauthClientClientIdRequestRequestStatus.INACTIVE:
            return inactive()
