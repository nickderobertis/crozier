

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error422Name(enum.StrEnum):
    UNPROCESSABLE_ENTITY = "UNPROCESSABLE_ENTITY"

    def visit(self, unprocessable_entity: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error422Name.UNPROCESSABLE_ENTITY:
            return unprocessable_entity()
