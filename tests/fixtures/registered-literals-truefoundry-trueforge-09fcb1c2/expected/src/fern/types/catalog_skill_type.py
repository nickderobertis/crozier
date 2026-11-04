

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogSkillType(enum.StrEnum):
    GIT = "git"

    def visit(self, git: typing.Callable[[], T_Result]) -> T_Result:
        if self is CatalogSkillType.GIT:
            return git()
