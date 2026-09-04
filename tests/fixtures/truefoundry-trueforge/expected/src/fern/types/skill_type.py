

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkillType(enum.StrEnum):
    GIT = "git"

    def visit(self, git: typing.Callable[[], T_Result]) -> T_Result:
        if self is SkillType.GIT:
            return git()
