

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MutationStrictObjectPayloadProfileSource(enum.StrEnum):
    MANUAL = "manual"
    SYNC = "sync"

    def visit(self, manual: typing.Callable[[], T_Result], sync: typing.Callable[[], T_Result]) -> T_Result:
        if self is MutationStrictObjectPayloadProfileSource.MANUAL:
            return manual()
        if self is MutationStrictObjectPayloadProfileSource.SYNC:
            return sync()
