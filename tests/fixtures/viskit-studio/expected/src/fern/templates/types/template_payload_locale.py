

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatePayloadLocale(enum.StrEnum):
    ZH = "zh"
    EN = "en"

    def visit(self, zh: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is TemplatePayloadLocale.ZH:
            return zh()
        if self is TemplatePayloadLocale.EN:
            return en()
