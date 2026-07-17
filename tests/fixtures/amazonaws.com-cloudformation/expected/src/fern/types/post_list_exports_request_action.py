

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostListExportsRequestAction(enum.StrEnum):
    LIST_EXPORTS = "ListExports"

    def visit(self, list_exports: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListExportsRequestAction.LIST_EXPORTS:
            return list_exports()
