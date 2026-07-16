

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UpdateStackSetInputOperationPreferencesRegionConcurrencyType(str, enum.Enum):
    """
    The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.
    """

    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"

    def visit(self, sequential: typing.Callable[[], T_Result], parallel: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateStackSetInputOperationPreferencesRegionConcurrencyType.SEQUENTIAL:
            return sequential()
        if self is UpdateStackSetInputOperationPreferencesRegionConcurrencyType.PARALLEL:
            return parallel()
