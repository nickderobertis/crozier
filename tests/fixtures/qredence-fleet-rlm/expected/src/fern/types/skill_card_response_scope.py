

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkillCardResponseScope(enum.StrEnum):
    SYSTEM = "system"
    WORKSPACE = "workspace"

    def visit(self, system: typing.Callable[[], T_Result], workspace: typing.Callable[[], T_Result]) -> T_Result:
        if self is SkillCardResponseScope.SYSTEM:
            return system()
        if self is SkillCardResponseScope.WORKSPACE:
            return workspace()
