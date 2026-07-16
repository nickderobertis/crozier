

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListStackResourcesRequestAction(str, enum.Enum):
    LIST_STACK_RESOURCES = "ListStackResources"

    def visit(self, list_stack_resources: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListStackResourcesRequestAction.LIST_STACK_RESOURCES:
            return list_stack_resources()
