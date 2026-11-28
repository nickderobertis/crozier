

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FormRawStringQueryValuePartType(enum.StrEnum):
    RAW_STRING = "RAW_STRING"

    def visit(self, raw_string: typing.Callable[[], T_Result]) -> T_Result:
        if self is FormRawStringQueryValuePartType.RAW_STRING:
            return raw_string()
