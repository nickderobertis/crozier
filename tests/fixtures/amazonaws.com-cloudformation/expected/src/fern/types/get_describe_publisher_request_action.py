

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribePublisherRequestAction(str, enum.Enum):
    DESCRIBE_PUBLISHER = "DescribePublisher"

    def visit(self, describe_publisher: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribePublisherRequestAction.DESCRIBE_PUBLISHER:
            return describe_publisher()
