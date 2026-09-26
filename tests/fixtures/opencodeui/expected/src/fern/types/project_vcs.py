

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectVcs(enum.StrEnum):
    GIT = "git"

    def visit(self, git: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectVcs.GIT:
            return git()
