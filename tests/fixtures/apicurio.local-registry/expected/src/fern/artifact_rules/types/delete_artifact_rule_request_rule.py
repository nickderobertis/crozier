

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteArtifactRuleRequestRule(enum.StrEnum):
    VALIDITY = "VALIDITY"
    COMPATIBILITY = "COMPATIBILITY"

    def visit(self, validity: typing.Callable[[], T_Result], compatibility: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteArtifactRuleRequestRule.VALIDITY:
            return validity()
        if self is DeleteArtifactRuleRequestRule.COMPATIBILITY:
            return compatibility()
