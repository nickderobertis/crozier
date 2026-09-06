

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAllBooksDeprecatedRequestMediaStatusItem(enum.StrEnum):
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
        if self is GetAllBooksDeprecatedRequestMediaStatusItem.UNKNOWN:
            return unknown()
        if self is GetAllBooksDeprecatedRequestMediaStatusItem.ERROR:
            return error()
        if self is GetAllBooksDeprecatedRequestMediaStatusItem.READY:
            return ready()
        if self is GetAllBooksDeprecatedRequestMediaStatusItem.UNSUPPORTED:
            return unsupported()
        if self is GetAllBooksDeprecatedRequestMediaStatusItem.OUTDATED:
            return outdated()
