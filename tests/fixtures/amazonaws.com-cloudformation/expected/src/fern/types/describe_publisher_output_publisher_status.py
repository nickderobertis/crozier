

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DescribePublisherOutputPublisherStatus(str, enum.Enum):
    """
    Whether the publisher is verified. Currently, all registered publishers are verified.
    """

    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"

    def visit(self, verified: typing.Callable[[], T_Result], unverified: typing.Callable[[], T_Result]) -> T_Result:
        if self is DescribePublisherOutputPublisherStatus.VERIFIED:
            return verified()
        if self is DescribePublisherOutputPublisherStatus.UNVERIFIED:
            return unverified()
