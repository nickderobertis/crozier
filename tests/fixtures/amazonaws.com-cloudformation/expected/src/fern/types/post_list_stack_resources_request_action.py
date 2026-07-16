

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostListStackResourcesRequestAction(enum.StrEnum):
    LIST_STACK_RESOURCES = "ListStackResources"

    def visit(self, list_stack_resources: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListStackResourcesRequestAction.LIST_STACK_RESOURCES:
            return list_stack_resources()
