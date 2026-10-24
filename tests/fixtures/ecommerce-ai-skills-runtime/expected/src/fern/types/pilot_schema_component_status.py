

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotSchemaComponentStatus(enum.StrEnum):
    READY = "ready"

    def visit(self, ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is PilotSchemaComponentStatus.READY:
            return ready()
