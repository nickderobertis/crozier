

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatchlistScreeningIndividualUpdateRequestResettableField(enum.StrEnum):
    """
    The name of a field that can be reset back to null
    """

    ASSIGNEE = "assignee"

    def visit(self, assignee: typing.Callable[[], T_Result]) -> T_Result:
        if self is WatchlistScreeningIndividualUpdateRequestResettableField.ASSIGNEE:
            return assignee()
