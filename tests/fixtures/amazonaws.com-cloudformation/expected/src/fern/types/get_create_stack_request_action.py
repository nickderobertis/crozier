

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetCreateStackRequestAction(str, enum.Enum):
    CREATE_STACK = "CreateStack"

    def visit(self, create_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCreateStackRequestAction.CREATE_STACK:
            return create_stack()
