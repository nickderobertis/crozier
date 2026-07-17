

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribePublisherOutputPublisherStatus(enum.StrEnum):
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
