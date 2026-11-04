

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistTagRuleInputMatch(enum.StrEnum):
    ANY = "any"
    ALL = "all"

    def visit(self, any: typing.Callable[[], T_Result], all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlaylistTagRuleInputMatch.ANY:
            return any()
        if self is PlaylistTagRuleInputMatch.ALL:
            return all_()
