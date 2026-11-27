

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConstraintStatusStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    COMPUTING = "COMPUTING"
    INACTIVE = "INACTIVE"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        computing: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConstraintStatusStatus.ACTIVE:
            return active()
        if self is ConstraintStatusStatus.COMPUTING:
            return computing()
        if self is ConstraintStatusStatus.INACTIVE:
            return inactive()
