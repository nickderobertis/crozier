

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetBatchDescribeTypeConfigurationsRequestAction(str, enum.Enum):
    BATCH_DESCRIBE_TYPE_CONFIGURATIONS = "BatchDescribeTypeConfigurations"

    def visit(self, batch_describe_type_configurations: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetBatchDescribeTypeConfigurationsRequestAction.BATCH_DESCRIBE_TYPE_CONFIGURATIONS:
            return batch_describe_type_configurations()
