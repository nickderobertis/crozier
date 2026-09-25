

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionalActionType(enum.StrEnum):
    """
    Action type; determines which payload fields are relevant.
    """

    JUMP_TO_PAGE = "JUMP_TO_PAGE"
    CALCULATE = "CALCULATE"
    REQUIRE_ANSWER = "REQUIRE_ANSWER"
    SHOW_BLOCKS = "SHOW_BLOCKS"
    HIDE_BLOCKS = "HIDE_BLOCKS"
    HIDE_BUTTON_TO_DISABLE_COMPLETION = "HIDE_BUTTON_TO_DISABLE_COMPLETION"

    def visit(
        self,
        jump_to_page: typing.Callable[[], T_Result],
        calculate: typing.Callable[[], T_Result],
        require_answer: typing.Callable[[], T_Result],
        show_blocks: typing.Callable[[], T_Result],
        hide_blocks: typing.Callable[[], T_Result],
        hide_button_to_disable_completion: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConditionalActionType.JUMP_TO_PAGE:
            return jump_to_page()
        if self is ConditionalActionType.CALCULATE:
            return calculate()
        if self is ConditionalActionType.REQUIRE_ANSWER:
            return require_answer()
        if self is ConditionalActionType.SHOW_BLOCKS:
            return show_blocks()
        if self is ConditionalActionType.HIDE_BLOCKS:
            return hide_blocks()
        if self is ConditionalActionType.HIDE_BUTTON_TO_DISABLE_COMPLETION:
            return hide_button_to_disable_completion()
