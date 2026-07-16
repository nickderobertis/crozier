

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListImportsRequestAction(str, enum.Enum):
    LIST_IMPORTS = "ListImports"

    def visit(self, list_imports: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListImportsRequestAction.LIST_IMPORTS:
            return list_imports()
