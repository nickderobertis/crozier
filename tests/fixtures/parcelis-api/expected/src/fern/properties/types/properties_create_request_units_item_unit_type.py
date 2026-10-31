

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PropertiesCreateRequestUnitsItemUnitType(enum.StrEnum):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"

    def visit(self, residential: typing.Callable[[], T_Result], commercial: typing.Callable[[], T_Result]) -> T_Result:
        if self is PropertiesCreateRequestUnitsItemUnitType.RESIDENTIAL:
            return residential()
        if self is PropertiesCreateRequestUnitsItemUnitType.COMMERCIAL:
            return commercial()
