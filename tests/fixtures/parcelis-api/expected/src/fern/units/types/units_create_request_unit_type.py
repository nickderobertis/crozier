

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UnitsCreateRequestUnitType(enum.StrEnum):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"

    def visit(self, residential: typing.Callable[[], T_Result], commercial: typing.Callable[[], T_Result]) -> T_Result:
        if self is UnitsCreateRequestUnitType.RESIDENTIAL:
            return residential()
        if self is UnitsCreateRequestUnitType.COMMERCIAL:
            return commercial()
