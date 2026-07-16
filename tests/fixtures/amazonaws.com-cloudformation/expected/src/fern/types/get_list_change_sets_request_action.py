

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListChangeSetsRequestAction(str, enum.Enum):
    LIST_CHANGE_SETS = "ListChangeSets"

    def visit(self, list_change_sets: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListChangeSetsRequestAction.LIST_CHANGE_SETS:
            return list_change_sets()
