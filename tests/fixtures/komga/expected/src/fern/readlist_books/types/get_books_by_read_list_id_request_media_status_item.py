

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBooksByReadListIdRequestMediaStatusItem(enum.StrEnum):
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
    READY = "READY"
    UNSUPPORTED = "UNSUPPORTED"
    OUTDATED = "OUTDATED"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        unsupported: typing.Callable[[], T_Result],
        outdated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBooksByReadListIdRequestMediaStatusItem.UNKNOWN:
            return unknown()
        if self is GetBooksByReadListIdRequestMediaStatusItem.ERROR:
            return error()
        if self is GetBooksByReadListIdRequestMediaStatusItem.READY:
            return ready()
        if self is GetBooksByReadListIdRequestMediaStatusItem.UNSUPPORTED:
            return unsupported()
        if self is GetBooksByReadListIdRequestMediaStatusItem.OUTDATED:
            return outdated()
