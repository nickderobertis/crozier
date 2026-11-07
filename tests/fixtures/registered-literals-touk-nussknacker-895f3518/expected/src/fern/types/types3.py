

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types3(enum.StrEnum):
    TYPED_OBJECT_TYPING_RESULT = "TypedObjectTypingResult"

    def visit(self, typed_object_typing_result: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types3.TYPED_OBJECT_TYPING_RESULT:
            return typed_object_typing_result()
