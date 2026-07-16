

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetImportStacksToStackSetRequestOperationPreferencesRegionConcurrencyType(enum.StrEnum):
    """
    The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.
    """

    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"

    def visit(self, sequential: typing.Callable[[], T_Result], parallel: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetImportStacksToStackSetRequestOperationPreferencesRegionConcurrencyType.SEQUENTIAL:
            return sequential()
        if self is GetImportStacksToStackSetRequestOperationPreferencesRegionConcurrencyType.PARALLEL:
            return parallel()
