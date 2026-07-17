

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostListTypesRequestAction(enum.StrEnum):
    LIST_TYPES = "ListTypes"

    def visit(self, list_types: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListTypesRequestAction.LIST_TYPES:
            return list_types()
