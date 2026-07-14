

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LanguageType(str, enum.Enum):
    STANDARD = "Standard"
    EXOTIC = "Exotic"

    def visit(self, standard: typing.Callable[[], T_Result], exotic: typing.Callable[[], T_Result]) -> T_Result:
        if self is LanguageType.STANDARD:
            return standard()
        if self is LanguageType.EXOTIC:
            return exotic()
