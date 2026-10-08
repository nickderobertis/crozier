

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExportAvailabilityResponseSource(enum.StrEnum):
    SERVER = "server"

    def visit(self, server: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExportAvailabilityResponseSource.SERVER:
            return server()
