

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisplayConfigDataframes(enum.StrEnum):
    PLAIN = "plain"
    RICH = "rich"

    def visit(self, plain: typing.Callable[[], T_Result], rich: typing.Callable[[], T_Result]) -> T_Result:
        if self is DisplayConfigDataframes.PLAIN:
            return plain()
        if self is DisplayConfigDataframes.RICH:
            return rich()
