

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelIdsSharedOne(enum.StrEnum):
    ID = "id"
    IDS = "ids"

    def visit(self, id: typing.Callable[[], T_Result], ids: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelIdsSharedOne.ID:
            return id()
        if self is ModelIdsSharedOne.IDS:
            return ids()
