

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UnitTypeTermValue(enum.StrEnum):
    TIME = "TIME"
    LENGTH = "LENGTH"
    MASS = "MASS"
    CURRENT = "CURRENT"
    TEMPERATURE = "TEMPERATURE"
    AMOUNT = "AMOUNT"
    LUMINOUS_INTENSITY = "LUMINOUS_INTENSITY"

    def visit(
        self,
        time: typing.Callable[[], T_Result],
        length: typing.Callable[[], T_Result],
        mass: typing.Callable[[], T_Result],
        current: typing.Callable[[], T_Result],
        temperature: typing.Callable[[], T_Result],
        amount: typing.Callable[[], T_Result],
        luminous_intensity: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UnitTypeTermValue.TIME:
            return time()
        if self is UnitTypeTermValue.LENGTH:
            return length()
        if self is UnitTypeTermValue.MASS:
            return mass()
        if self is UnitTypeTermValue.CURRENT:
            return current()
        if self is UnitTypeTermValue.TEMPERATURE:
            return temperature()
        if self is UnitTypeTermValue.AMOUNT:
            return amount()
        if self is UnitTypeTermValue.LUMINOUS_INTENSITY:
            return luminous_intensity()
