

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SelectedFulfillmentOptionOneType(enum.StrEnum):
    DIGITAL = "digital"

    def visit(self, digital: typing.Callable[[], T_Result]) -> T_Result:
        if self is SelectedFulfillmentOptionOneType.DIGITAL:
            return digital()
