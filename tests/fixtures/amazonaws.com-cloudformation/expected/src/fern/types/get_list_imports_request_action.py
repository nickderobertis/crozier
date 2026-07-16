

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListImportsRequestAction(enum.StrEnum):
    LIST_IMPORTS = "ListImports"

    def visit(self, list_imports: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListImportsRequestAction.LIST_IMPORTS:
            return list_imports()
