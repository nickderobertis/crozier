

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactPointUse(enum.StrEnum):
    HOME = "HOME"
    WORK = "WORK"
    TEMP = "TEMP"
    OLD = "OLD"
    MOBILE = "MOBILE"
    NULL = "NULL"

    def visit(
        self,
        home: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
        temp: typing.Callable[[], T_Result],
        old: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactPointUse.HOME:
            return home()
        if self is ContactPointUse.WORK:
            return work()
        if self is ContactPointUse.TEMP:
            return temp()
        if self is ContactPointUse.OLD:
            return old()
        if self is ContactPointUse.MOBILE:
            return mobile()
        if self is ContactPointUse.NULL:
            return null()
