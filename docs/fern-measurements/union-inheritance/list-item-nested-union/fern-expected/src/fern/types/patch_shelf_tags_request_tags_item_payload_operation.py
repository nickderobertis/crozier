

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchShelfTagsRequestTagsItemPayloadOperation(enum.StrEnum):
    CREATE = "create"
    UPDATE = "update"

    def visit(self, create: typing.Callable[[], T_Result], update: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchShelfTagsRequestTagsItemPayloadOperation.CREATE:
            return create()
        if self is PatchShelfTagsRequestTagsItemPayloadOperation.UPDATE:
            return update()
