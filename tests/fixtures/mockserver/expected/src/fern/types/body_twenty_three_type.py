

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyTwentyThreeType(enum.StrEnum):
    XPATH = "XPATH"

    def visit(self, xpath: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyTwentyThreeType.XPATH:
            return xpath()
