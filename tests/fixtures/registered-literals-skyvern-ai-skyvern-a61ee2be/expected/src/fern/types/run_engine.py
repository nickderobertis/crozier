

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunEngine(enum.StrEnum):
    SKYVERN10 = "skyvern-1.0"
    SKYVERN20 = "skyvern-2.0"
    SKYVERN30 = "skyvern-3.0"
    OPENAI_CUA = "openai-cua"
    ANTHROPIC_CUA = "anthropic-cua"
    UI_TARS = "ui-tars"
    YUTORI_NAVIGATOR = "yutori-navigator"

    def visit(
        self,
        skyvern10: typing.Callable[[], T_Result],
        skyvern20: typing.Callable[[], T_Result],
        skyvern30: typing.Callable[[], T_Result],
        openai_cua: typing.Callable[[], T_Result],
        anthropic_cua: typing.Callable[[], T_Result],
        ui_tars: typing.Callable[[], T_Result],
        yutori_navigator: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunEngine.SKYVERN10:
            return skyvern10()
        if self is RunEngine.SKYVERN20:
            return skyvern20()
        if self is RunEngine.SKYVERN30:
            return skyvern30()
        if self is RunEngine.OPENAI_CUA:
            return openai_cua()
        if self is RunEngine.ANTHROPIC_CUA:
            return anthropic_cua()
        if self is RunEngine.UI_TARS:
            return ui_tars()
        if self is RunEngine.YUTORI_NAVIGATOR:
            return yutori_navigator()
