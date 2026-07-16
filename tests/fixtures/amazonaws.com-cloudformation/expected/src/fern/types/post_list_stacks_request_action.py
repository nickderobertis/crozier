

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListStacksRequestAction(str, enum.Enum):
    LIST_STACKS = "ListStacks"

    def visit(self, list_stacks: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListStacksRequestAction.LIST_STACKS:
            return list_stacks()
