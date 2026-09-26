

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationJobCreateLocale(enum.StrEnum):
    ZH = "zh"
    EN = "en"

    def visit(self, zh: typing.Callable[[], T_Result], en: typing.Callable[[], T_Result]) -> T_Result:
        if self is GenerationJobCreateLocale.ZH:
            return zh()
        if self is GenerationJobCreateLocale.EN:
            return en()
