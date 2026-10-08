

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SetNameType(enum.StrEnum):
    SET_NAME = "set-name"

    def visit(self, set_name: typing.Callable[[], T_Result]) -> T_Result:
        if self is SetNameType.SET_NAME:
            return set_name()
