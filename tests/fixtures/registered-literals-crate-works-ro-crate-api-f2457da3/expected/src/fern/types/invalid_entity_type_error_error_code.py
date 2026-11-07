

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvalidEntityTypeErrorErrorCode(enum.StrEnum):
    INVALID_ENTITY_TYPE = "INVALID_ENTITY_TYPE"

    def visit(self, invalid_entity_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is InvalidEntityTypeErrorErrorCode.INVALID_ENTITY_TYPE:
            return invalid_entity_type()
