

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DestinationStripeConfigWriteMode(enum.StrEnum):
    CREATE = "create"

    def visit(self, create: typing.Callable[[], T_Result]) -> T_Result:
        if self is DestinationStripeConfigWriteMode.CREATE:
            return create()
