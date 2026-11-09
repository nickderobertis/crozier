

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RequestsFilterType(enum.StrEnum):
    """
    The type of filter to apply.  `in` filters will limit results to only the specified values, while `not_in` filters will exclude the specified values.
    """

    IN = "in"
    NOT_IN = "not_in"

    def visit(self, in_: typing.Callable[[], T_Result], not_in: typing.Callable[[], T_Result]) -> T_Result:
        if self is RequestsFilterType.IN:
            return in_()
        if self is RequestsFilterType.NOT_IN:
            return not_in()
