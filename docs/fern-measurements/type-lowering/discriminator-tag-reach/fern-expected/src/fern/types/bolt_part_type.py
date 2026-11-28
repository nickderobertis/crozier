

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BoltPartType(enum.StrEnum):
    BOLT = "BOLT"

    def visit(self, bolt: typing.Callable[[], T_Result]) -> T_Result:
        if self is BoltPartType.BOLT:
            return bolt()
