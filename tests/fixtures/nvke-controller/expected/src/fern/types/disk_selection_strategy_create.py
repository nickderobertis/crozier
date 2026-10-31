

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DiskSelectionStrategyCreate(enum.StrEnum):
    """
    Which disk the OS is installed on. Default smallest.
    """

    SMALLEST = "smallest"
    LARGEST = "largest"

    def visit(self, smallest: typing.Callable[[], T_Result], largest: typing.Callable[[], T_Result]) -> T_Result:
        if self is DiskSelectionStrategyCreate.SMALLEST:
            return smallest()
        if self is DiskSelectionStrategyCreate.LARGEST:
            return largest()
