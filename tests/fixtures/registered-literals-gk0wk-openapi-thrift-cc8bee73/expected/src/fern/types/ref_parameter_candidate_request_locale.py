

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RefParameterCandidateRequestLocale(enum.StrEnum):
    ZH_CN = "zh-CN"
    EN_US = "en-US"

    def visit(self, zh_cn: typing.Callable[[], T_Result], en_us: typing.Callable[[], T_Result]) -> T_Result:
        if self is RefParameterCandidateRequestLocale.ZH_CN:
            return zh_cn()
        if self is RefParameterCandidateRequestLocale.EN_US:
            return en_us()
