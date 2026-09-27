

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateDriftAlertSettingsRequestLocale(enum.StrEnum):
    RU = "ru"
    EN = "en"

    def visit(self, ru: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateDriftAlertSettingsRequestLocale.RU:
            return ru()
        if self is UpdateDriftAlertSettingsRequestLocale.EN:
            return en()
