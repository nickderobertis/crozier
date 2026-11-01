

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DiskSelectionStrategy(enum.StrEnum):
    """
    Which disk the OS is installed on. Default smallest.
    """

    SMALLEST = "smallest"
    LARGEST = "largest"

    def visit(self, smallest: typing.Callable[[], T_Result], largest: typing.Callable[[], T_Result]) -> T_Result:
        if self is DiskSelectionStrategy.SMALLEST:
            return smallest()
        if self is DiskSelectionStrategy.LARGEST:
            return largest()
