

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtendedLegacyValType(enum.StrEnum):
    """
    The type of a val. HTTP can receive web requests, Email can receive emails, Cron runs periodically, and Script can be used for libraries or one-off calculations
    """

    INTERVAL = "interval"
    HTTP = "http"
    EXPRESS = "express"
    EMAIL = "email"
    SCRIPT = "script"
    RPC = "rpc"
    HTTPNEXT = "httpnext"

    def visit(
        self,
        interval: typing.Callable[[], T_Result],
        http: typing.Callable[[], T_Result],
        express: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        script: typing.Callable[[], T_Result],
        rpc: typing.Callable[[], T_Result],
        httpnext: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExtendedLegacyValType.INTERVAL:
            return interval()
        if self is ExtendedLegacyValType.HTTP:
            return http()
        if self is ExtendedLegacyValType.EXPRESS:
            return express()
        if self is ExtendedLegacyValType.EMAIL:
            return email()
        if self is ExtendedLegacyValType.SCRIPT:
            return script()
        if self is ExtendedLegacyValType.RPC:
            return rpc()
        if self is ExtendedLegacyValType.HTTPNEXT:
            return httpnext()
