

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionContentPartImageWithTitleImageUrlDetailOne(enum.StrEnum):
    LOW = "low"

    def visit(self, low: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionContentPartImageWithTitleImageUrlDetailOne.LOW:
            return low()
