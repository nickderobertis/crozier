

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class HangSignsRequestMotto(enum.StrEnum):
    THE_EARLY_BIRD = "the 'early' bird"
    PLAIN = "plain"

    def visit(self, the_early_bird: typing.Callable[[], T_Result], plain: typing.Callable[[], T_Result]) -> T_Result:
        if self is HangSignsRequestMotto.THE_EARLY_BIRD:
            return the_early_bird()
        if self is HangSignsRequestMotto.PLAIN:
            return plain()
