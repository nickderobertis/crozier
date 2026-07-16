

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListExportsRequestAction(str, enum.Enum):
    LIST_EXPORTS = "ListExports"

    def visit(self, list_exports: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListExportsRequestAction.LIST_EXPORTS:
            return list_exports()
