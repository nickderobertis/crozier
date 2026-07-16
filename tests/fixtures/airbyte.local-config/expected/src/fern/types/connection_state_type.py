

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionStateType(enum.StrEnum):
    GLOBAL = "global"
    STREAM = "stream"
    LEGACY = "legacy"
    NOT_SET = "not_set"

    def visit(
        self,
        global_: typing.Callable[[], T_Result],
        stream: typing.Callable[[], T_Result],
        legacy: typing.Callable[[], T_Result],
        not_set: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionStateType.GLOBAL:
            return global_()
        if self is ConnectionStateType.STREAM:
            return stream()
        if self is ConnectionStateType.LEGACY:
            return legacy()
        if self is ConnectionStateType.NOT_SET:
            return not_set()
