

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CacheConfigVerification(enum.StrEnum):
    OFF = "off"
    ON = "on"
    STRICT = "strict"

    def visit(
        self,
        off: typing.Callable[[], T_Result],
        on: typing.Callable[[], T_Result],
        strict: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CacheConfigVerification.OFF:
            return off()
        if self is CacheConfigVerification.ON:
            return on()
        if self is CacheConfigVerification.STRICT:
            return strict()
