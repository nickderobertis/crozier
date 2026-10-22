

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubAccountUsageResponseAllocationMethod(enum.StrEnum):
    """
    Method used to allocate the pooled parent invoice cost
    """

    PROPORTIONAL = "proportional"

    def visit(self, proportional: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubAccountUsageResponseAllocationMethod.PROPORTIONAL:
            return proportional()
