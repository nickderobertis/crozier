

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SchemePayloadLocale(enum.StrEnum):
    ZH = "zh"
    EN = "en"

    def visit(self, zh: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is SchemePayloadLocale.ZH:
            return zh()
        if self is SchemePayloadLocale.EN:
            return en()
