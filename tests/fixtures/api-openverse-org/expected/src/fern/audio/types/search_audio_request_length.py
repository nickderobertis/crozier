

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchAudioRequestLength(enum.StrEnum):
    SHORTEST = "shortest"
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

    def visit(
        self,
        shortest: typing.Callable[[], T_Result],
        short: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        long_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchAudioRequestLength.SHORTEST:
            return shortest()
        if self is SearchAudioRequestLength.SHORT:
            return short()
        if self is SearchAudioRequestLength.MEDIUM:
            return medium()
        if self is SearchAudioRequestLength.LONG:
            return long_()
