

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostUpdateStackRequestAction(str, enum.Enum):
    UPDATE_STACK = "UpdateStack"

    def visit(self, update_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostUpdateStackRequestAction.UPDATE_STACK:
            return update_stack()
