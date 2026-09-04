

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestStatus(enum.StrEnum):
    """
    Status of the Client.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestStatus.ACTIVE:
            return active()
        if self is PatchClientClientIdRequestRequestStatus.INACTIVE:
            return inactive()
