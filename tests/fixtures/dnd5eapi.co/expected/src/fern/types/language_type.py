

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LanguageType(enum.StrEnum):
    STANDARD = "Standard"
    EXOTIC = "Exotic"

    def visit(self, standard: typing.Callable[[], T_Result], exotic: typing.Callable[[], T_Result]) -> T_Result:
        if self is LanguageType.STANDARD:
            return standard()
        if self is LanguageType.EXOTIC:
            return exotic()
