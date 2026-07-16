

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListExportsRequestAction(str, enum.Enum):
    LIST_EXPORTS = "ListExports"

    def visit(self, list_exports: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListExportsRequestAction.LIST_EXPORTS:
            return list_exports()
