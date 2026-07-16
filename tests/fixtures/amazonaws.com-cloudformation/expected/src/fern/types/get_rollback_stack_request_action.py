

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetRollbackStackRequestAction(str, enum.Enum):
    ROLLBACK_STACK = "RollbackStack"

    def visit(self, rollback_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRollbackStackRequestAction.ROLLBACK_STACK:
            return rollback_stack()
