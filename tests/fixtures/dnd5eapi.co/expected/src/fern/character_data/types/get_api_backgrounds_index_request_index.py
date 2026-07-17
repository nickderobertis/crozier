

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiBackgroundsIndexRequestIndex(enum.StrEnum):
    ACOLYTE = "acolyte"

    def visit(self, acolyte: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetApiBackgroundsIndexRequestIndex.ACOLYTE:
            return acolyte()
