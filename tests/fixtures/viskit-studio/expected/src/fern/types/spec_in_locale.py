

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpecInLocale(enum.StrEnum):
    ZH = "zh"
    EN = "en"

    def visit(self, zh: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpecInLocale.ZH:
            return zh()
        if self is SpecInLocale.EN:
            return en()
