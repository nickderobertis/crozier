

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListTypesRequestAction(str, enum.Enum):
    LIST_TYPES = "ListTypes"

    def visit(self, list_types: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListTypesRequestAction.LIST_TYPES:
            return list_types()
