

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartialDirectConversionParametersType(enum.StrEnum):
    DIRECT = "direct"

    def visit(self, direct: typing.Callable[[], T_Result]) -> T_Result:
        if self is PartialDirectConversionParametersType.DIRECT:
            return direct()
