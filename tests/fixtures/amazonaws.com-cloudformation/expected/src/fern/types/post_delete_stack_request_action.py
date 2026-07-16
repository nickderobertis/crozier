

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDeleteStackRequestAction(enum.StrEnum):
    DELETE_STACK = "DeleteStack"

    def visit(self, delete_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDeleteStackRequestAction.DELETE_STACK:
            return delete_stack()
