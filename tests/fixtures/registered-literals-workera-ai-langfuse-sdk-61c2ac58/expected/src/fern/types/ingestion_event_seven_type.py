

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventSevenType(enum.StrEnum):
    SDK_LOG = "sdk-log"

    def visit(self, sdk_log: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventSevenType.SDK_LOG:
            return sdk_log()
