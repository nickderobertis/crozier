

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusEnum(enum.StrEnum):
    """
    Current status of this resource
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is StatusEnum.ACTIVE:
            return active()
        if self is StatusEnum.INACTIVE:
            return inactive()
