

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderCategory(enum.StrEnum):
    BASE = "base"
    BYOK = "byok"

    def visit(self, base: typing.Callable[[], T_Result], byok: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProviderCategory.BASE:
            return base()
        if self is ProviderCategory.BYOK:
            return byok()
