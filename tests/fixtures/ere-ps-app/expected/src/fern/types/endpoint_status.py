

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EndpointStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    ERROR = "ERROR"
    OFF = "OFF"
    ENTEREDINERROR = "ENTEREDINERROR"
    TEST = "TEST"
    NULL = "NULL"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        suspended: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        off: typing.Callable[[], T_Result],
        enteredinerror: typing.Callable[[], T_Result],
        test: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EndpointStatus.ACTIVE:
            return active()
        if self is EndpointStatus.SUSPENDED:
            return suspended()
        if self is EndpointStatus.ERROR:
            return error()
        if self is EndpointStatus.OFF:
            return off()
        if self is EndpointStatus.ENTEREDINERROR:
            return enteredinerror()
        if self is EndpointStatus.TEST:
            return test()
        if self is EndpointStatus.NULL:
            return null()
