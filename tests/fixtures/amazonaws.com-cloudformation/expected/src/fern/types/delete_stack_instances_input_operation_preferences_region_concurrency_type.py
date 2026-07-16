

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType(str, enum.Enum):
    """
    The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.
    """

    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"

    def visit(self, sequential: typing.Callable[[], T_Result], parallel: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType.SEQUENTIAL:
            return sequential()
        if self is DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType.PARALLEL:
            return parallel()
