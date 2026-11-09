

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RequestsFilterTypeEmpty(enum.StrEnum):
    """
    The type of filter to apply.
    """

    EMPTY = "empty"
    NOT_EMPTY = "not_empty"

    def visit(self, empty: typing.Callable[[], T_Result], not_empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is RequestsFilterTypeEmpty.EMPTY:
            return empty()
        if self is RequestsFilterTypeEmpty.NOT_EMPTY:
            return not_empty()
