

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCreateStackRequestAction(enum.StrEnum):
    CREATE_STACK = "CreateStack"

    def visit(self, create_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCreateStackRequestAction.CREATE_STACK:
            return create_stack()
