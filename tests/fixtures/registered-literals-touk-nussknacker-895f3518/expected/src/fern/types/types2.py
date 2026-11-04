

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types2(enum.StrEnum):
    TYPED_DICT = "TypedDict"

    def visit(self, typed_dict: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types2.TYPED_DICT:
            return typed_dict()
