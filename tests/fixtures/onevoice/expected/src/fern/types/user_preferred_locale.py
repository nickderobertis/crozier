

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserPreferredLocale(enum.StrEnum):
    RU = "ru"
    EN = "en"

    def visit(self, ru: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserPreferredLocale.RU:
            return ru()
        if self is UserPreferredLocale.EN:
            return en()
