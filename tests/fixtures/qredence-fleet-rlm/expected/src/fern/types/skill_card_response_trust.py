

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkillCardResponseTrust(enum.StrEnum):
    SYSTEM = "system"
    WORKSPACE = "workspace"
    UNTRUSTED = "untrusted"

    def visit(
        self,
        system: typing.Callable[[], T_Result],
        workspace: typing.Callable[[], T_Result],
        untrusted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SkillCardResponseTrust.SYSTEM:
            return system()
        if self is SkillCardResponseTrust.WORKSPACE:
            return workspace()
        if self is SkillCardResponseTrust.UNTRUSTED:
            return untrusted()
