

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SupportedLocale(enum.StrEnum):
    EN = "en"
    ES_ES = "es_ES"
    KO_KR = "ko_KR"
    ZH_CN = "zh_CN"

    def visit(
        self,
        en: typing.Callable[[], T_Result],
        es_es: typing.Callable[[], T_Result],
        ko_kr: typing.Callable[[], T_Result],
        zh_cn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SupportedLocale.EN:
            return en()
        if self is SupportedLocale.ES_ES:
            return es_es()
        if self is SupportedLocale.KO_KR:
            return ko_kr()
        if self is SupportedLocale.ZH_CN:
            return zh_cn()
