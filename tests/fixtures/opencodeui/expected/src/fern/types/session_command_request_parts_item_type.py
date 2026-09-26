

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionCommandRequestPartsItemType(enum.StrEnum):
    FILE = "file"

    def visit(self, file: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionCommandRequestPartsItemType.FILE:
            return file()
