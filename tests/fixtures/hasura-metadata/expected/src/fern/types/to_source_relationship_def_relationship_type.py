

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToSourceRelationshipDefRelationshipType(enum.StrEnum):
    OBJECT = "object"
    ARRAY = "array"

    def visit(self, object: typing.Callable[[], T_Result], array: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToSourceRelationshipDefRelationshipType.OBJECT:
            return object()
        if self is ToSourceRelationshipDefRelationshipType.ARRAY:
            return array()
