

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TypeRelationshipDefinitionType(enum.StrEnum):
    OBJECT = "object"
    ARRAY = "array"

    def visit(self, object: typing.Callable[[], T_Result], array: typing.Callable[[], T_Result]) -> T_Result:
        if self is TypeRelationshipDefinitionType.OBJECT:
            return object()
        if self is TypeRelationshipDefinitionType.ARRAY:
            return array()
