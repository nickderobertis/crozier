

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiBackgroundsIndexRequestIndex(str, enum.Enum):
    ACOLYTE = "acolyte"

    def visit(self, acolyte: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetApiBackgroundsIndexRequestIndex.ACOLYTE:
            return acolyte()
