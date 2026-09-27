

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteMockserverPreemptionResponseState(enum.StrEnum):
    INACTIVE = "inactive"

    def visit(self, inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteMockserverPreemptionResponseState.INACTIVE:
            return inactive()
