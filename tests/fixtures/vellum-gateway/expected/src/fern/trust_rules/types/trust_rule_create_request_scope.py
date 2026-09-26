

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TrustRuleCreateRequestScope(enum.StrEnum):
    """
    Compatibility field. Trust rules apply workspace-wide: the engine matches on (tool, pattern) only, so a narrower scope cannot be honored and any value other than "everywhere" is rejected rather than stored broader than the consent it records.
    """

    EVERYWHERE = "everywhere"

    def visit(self, everywhere: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrustRuleCreateRequestScope.EVERYWHERE:
            return everywhere()
