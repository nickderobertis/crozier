

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionContentPartImageWithTitleImageUrlDetailTwo(enum.StrEnum):
    HIGH = "high"

    def visit(self, high: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionContentPartImageWithTitleImageUrlDetailTwo.HIGH:
            return high()
