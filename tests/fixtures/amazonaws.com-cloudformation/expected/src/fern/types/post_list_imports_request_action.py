

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListImportsRequestAction(str, enum.Enum):
    LIST_IMPORTS = "ListImports"

    def visit(self, list_imports: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListImportsRequestAction.LIST_IMPORTS:
            return list_imports()
