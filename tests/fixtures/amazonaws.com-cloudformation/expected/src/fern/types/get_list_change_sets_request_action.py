

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListChangeSetsRequestAction(enum.StrEnum):
    LIST_CHANGE_SETS = "ListChangeSets"

    def visit(self, list_change_sets: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListChangeSetsRequestAction.LIST_CHANGE_SETS:
            return list_change_sets()
