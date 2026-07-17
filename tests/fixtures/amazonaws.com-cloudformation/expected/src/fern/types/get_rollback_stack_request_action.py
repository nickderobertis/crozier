

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRollbackStackRequestAction(enum.StrEnum):
    ROLLBACK_STACK = "RollbackStack"

    def visit(self, rollback_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRollbackStackRequestAction.ROLLBACK_STACK:
            return rollback_stack()
