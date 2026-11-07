

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BasicLegacyValType(enum.StrEnum):
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
        if self is BasicLegacyValType.INTERVAL:
            return interval()
        if self is BasicLegacyValType.HTTP:
            return http()
        if self is BasicLegacyValType.EXPRESS:
            return express()
        if self is BasicLegacyValType.EMAIL:
            return email()
        if self is BasicLegacyValType.SCRIPT:
            return script()
        if self is BasicLegacyValType.RPC:
            return rpc()
        if self is BasicLegacyValType.HTTPNEXT:
            return httpnext()
