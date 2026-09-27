

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdatePreferredLocaleRequestLocale(enum.StrEnum):
    RU = "ru"
    EN = "en"

    def visit(self, ru: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdatePreferredLocaleRequestLocale.RU:
            return ru()
        if self is UpdatePreferredLocaleRequestLocale.EN:
            return en()
