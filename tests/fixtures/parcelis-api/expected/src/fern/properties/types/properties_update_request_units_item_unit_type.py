

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PropertiesUpdateRequestUnitsItemUnitType(enum.StrEnum):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"

    def visit(self, residential: typing.Callable[[], T_Result], commercial: typing.Callable[[], T_Result]) -> T_Result:
        if self is PropertiesUpdateRequestUnitsItemUnitType.RESIDENTIAL:
            return residential()
        if self is PropertiesUpdateRequestUnitsItemUnitType.COMMERCIAL:
            return commercial()
