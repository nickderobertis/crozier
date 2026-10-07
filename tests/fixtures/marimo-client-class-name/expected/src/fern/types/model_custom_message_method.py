

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelCustomMessageMethod(enum.StrEnum):
    CUSTOM = "custom"

    def visit(self, custom: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelCustomMessageMethod.CUSTOM:
            return custom()
