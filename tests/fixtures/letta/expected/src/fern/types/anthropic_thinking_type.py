

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnthropicThinkingType(enum.StrEnum):
    """
    The type of thinking to use.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is AnthropicThinkingType.ENABLED:
            return enabled()
        if self is AnthropicThinkingType.DISABLED:
            return disabled()
