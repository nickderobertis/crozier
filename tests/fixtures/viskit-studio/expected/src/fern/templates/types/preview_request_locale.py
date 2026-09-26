

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PreviewRequestLocale(enum.StrEnum):
    ZH = "zh"
    EN = "en"

    def visit(self, zh: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is PreviewRequestLocale.ZH:
            return zh()
        if self is PreviewRequestLocale.EN:
            return en()
