

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DestinationStripeConfigApiVersion(enum.StrEnum):
    UNSAFE_DEVELOPMENT = "unsafe-development"

    def visit(self, unsafe_development: typing.Callable[[], T_Result]) -> T_Result:
        if self is DestinationStripeConfigApiVersion.UNSAFE_DEVELOPMENT:
            return unsafe_development()
