

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListStacksRequestAction(str, enum.Enum):
    LIST_STACKS = "ListStacks"

    def visit(self, list_stacks: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListStacksRequestAction.LIST_STACKS:
            return list_stacks()
