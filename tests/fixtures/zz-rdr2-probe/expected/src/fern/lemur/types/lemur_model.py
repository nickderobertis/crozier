

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class LemurModel(enum.StrEnum):
    """
    The model that is used for the final prompt after compression is performed.
    """

    ANTHROPIC_CLAUDE_SONNET420250514 = "anthropic/claude-sonnet-4-20250514"
    ANTHROPIC_CLAUDE_OPUS420250514 = "anthropic/claude-opus-4-20250514"
    ANTHROPIC_CLAUDE37SONNET20250219 = "anthropic/claude-3-7-sonnet-20250219"
    ANTHROPIC_CLAUDE3_5_SONNET = "anthropic/claude-3-5-sonnet"
    """
    Claude 3.5 Sonnet is Anthropic's most intelligent model to date, outperforming Claude 3 Opus on a wide range of evaluations, with the speed and cost of Claude 3 Sonnet.
    """

    ANTHROPIC_CLAUDE35HAIKU20241022 = "anthropic/claude-3-5-haiku-20241022"
    ANTHROPIC_CLAUDE3_OPUS = "anthropic/claude-3-opus"
    """
    Claude 3 Opus is good at handling complex analysis, longer tasks with many steps, and higher-order math and coding tasks.
    """

    ANTHROPIC_CLAUDE3_HAIKU = "anthropic/claude-3-haiku"
    """
    Claude 3 Haiku is the fastest model that can execute lightweight actions.
    """

    def visit(
        self,
        anthropic_claude_sonnet420250514: typing.Callable[[], T_Result],
        anthropic_claude_opus420250514: typing.Callable[[], T_Result],
        anthropic_claude37sonnet20250219: typing.Callable[[], T_Result],
        anthropic_claude3_5_sonnet: typing.Callable[[], T_Result],
        anthropic_claude35haiku20241022: typing.Callable[[], T_Result],
        anthropic_claude3_opus: typing.Callable[[], T_Result],
        anthropic_claude3_haiku: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LemurModel.ANTHROPIC_CLAUDE_SONNET420250514:
            return anthropic_claude_sonnet420250514()
        if self is LemurModel.ANTHROPIC_CLAUDE_OPUS420250514:
            return anthropic_claude_opus420250514()
        if self is LemurModel.ANTHROPIC_CLAUDE37SONNET20250219:
            return anthropic_claude37sonnet20250219()
        if self is LemurModel.ANTHROPIC_CLAUDE3_5_SONNET:
            return anthropic_claude3_5_sonnet()
        if self is LemurModel.ANTHROPIC_CLAUDE35HAIKU20241022:
            return anthropic_claude35haiku20241022()
        if self is LemurModel.ANTHROPIC_CLAUDE3_OPUS:
            return anthropic_claude3_opus()
        if self is LemurModel.ANTHROPIC_CLAUDE3_HAIKU:
            return anthropic_claude3_haiku()
