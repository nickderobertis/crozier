

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostRollbackStackRequestAction(str, enum.Enum):
    ROLLBACK_STACK = "RollbackStack"

    def visit(self, rollback_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostRollbackStackRequestAction.ROLLBACK_STACK:
            return rollback_stack()
