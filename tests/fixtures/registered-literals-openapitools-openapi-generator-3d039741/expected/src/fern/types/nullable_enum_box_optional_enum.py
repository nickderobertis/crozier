

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NullableEnumBoxOptionalEnum(enum.StrEnum):
    STANDARD = "standard"
    HD = "hd"

    def visit(self, standard: typing.Callable[[], T_Result], hd: typing.Callable[[], T_Result]) -> T_Result:
        if self is NullableEnumBoxOptionalEnum.STANDARD:
            return standard()
        if self is NullableEnumBoxOptionalEnum.HD:
            return hd()
