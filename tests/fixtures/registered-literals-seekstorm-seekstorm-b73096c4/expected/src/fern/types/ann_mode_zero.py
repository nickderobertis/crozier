

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnnModeZero(enum.StrEnum):
    """
    Search in all clusters (default)
    """

    ALL = "All"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is AnnModeZero.ALL:
            return all_()
