

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PropertiesByIdResponseDataUnitStatusesItemZero(enum.StrEnum):
    VACANT = "vacant"

    def visit(self, vacant: typing.Callable[[], T_Result]) -> T_Result:
        if self is PropertiesByIdResponseDataUnitStatusesItemZero.VACANT:
            return vacant()
