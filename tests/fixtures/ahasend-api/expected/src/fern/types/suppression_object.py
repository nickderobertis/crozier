

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SuppressionObject(enum.StrEnum):
    """
    Object type identifier
    """

    SUPPRESSION = "suppression"

    def visit(self, suppression: typing.Callable[[], T_Result]) -> T_Result:
        if self is SuppressionObject.SUPPRESSION:
            return suppression()
