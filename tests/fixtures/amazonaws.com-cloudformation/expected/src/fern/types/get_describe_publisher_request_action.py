

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDescribePublisherRequestAction(enum.StrEnum):
    DESCRIBE_PUBLISHER = "DescribePublisher"

    def visit(self, describe_publisher: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribePublisherRequestAction.DESCRIBE_PUBLISHER:
            return describe_publisher()
