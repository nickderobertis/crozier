

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListTypesRequestAction(str, enum.Enum):
    LIST_TYPES = "ListTypes"

    def visit(self, list_types: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListTypesRequestAction.LIST_TYPES:
            return list_types()
