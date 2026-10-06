

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AddressType(enum.StrEnum):
    POSTAL = "POSTAL"
    PHYSICAL = "PHYSICAL"
    BOTH = "BOTH"
    NULL = "NULL"

    def visit(
        self,
        postal: typing.Callable[[], T_Result],
        physical: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressType.POSTAL:
            return postal()
        if self is AddressType.PHYSICAL:
            return physical()
        if self is AddressType.BOTH:
            return both()
        if self is AddressType.NULL:
            return null()
