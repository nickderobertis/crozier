

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AddressUse(enum.StrEnum):
    HOME = "HOME"
    WORK = "WORK"
    TEMP = "TEMP"
    OLD = "OLD"
    BILLING = "BILLING"
    NULL = "NULL"

    def visit(
        self,
        home: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
        temp: typing.Callable[[], T_Result],
        old: typing.Callable[[], T_Result],
        billing: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressUse.HOME:
            return home()
        if self is AddressUse.WORK:
            return work()
        if self is AddressUse.TEMP:
            return temp()
        if self is AddressUse.OLD:
            return old()
        if self is AddressUse.BILLING:
            return billing()
        if self is AddressUse.NULL:
            return null()
