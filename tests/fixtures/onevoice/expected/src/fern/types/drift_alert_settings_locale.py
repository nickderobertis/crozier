

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DriftAlertSettingsLocale(enum.StrEnum):
    RU = "ru"
    EN = "en"

    def visit(self, ru: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is DriftAlertSettingsLocale.RU:
            return ru()
        if self is DriftAlertSettingsLocale.EN:
            return en()
