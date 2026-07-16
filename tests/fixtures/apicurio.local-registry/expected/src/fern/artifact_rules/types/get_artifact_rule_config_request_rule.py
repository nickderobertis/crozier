

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetArtifactRuleConfigRequestRule(enum.StrEnum):
    VALIDITY = "VALIDITY"
    COMPATIBILITY = "COMPATIBILITY"

    def visit(self, validity: typing.Callable[[], T_Result], compatibility: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetArtifactRuleConfigRequestRule.VALIDITY:
            return validity()
        if self is GetArtifactRuleConfigRequestRule.COMPATIBILITY:
            return compatibility()
