

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HoState(enum.StrEnum):
    NONE = "NONE"
    PREPARING = "PREPARING"
    PREPARED = "PREPARED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        preparing: typing.Callable[[], T_Result],
        prepared: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HoState.NONE:
            return none()
        if self is HoState.PREPARING:
            return preparing()
        if self is HoState.PREPARED:
            return prepared()
        if self is HoState.COMPLETED:
            return completed()
        if self is HoState.CANCELLED:
            return cancelled()
