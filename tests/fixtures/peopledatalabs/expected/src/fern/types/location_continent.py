

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationContinent(enum.StrEnum):
    """
    the canonical continent of the location
    """

    AFRICA = "africa"
    ANTARCTICA = "antarctica"
    ASIA = "asia"
    EUROPE = "europe"
    NORTH_AMERICA = "north america"
    OCEANIA = "oceania"
    SOUTH_AMERICA = "south america"

    def visit(
        self,
        africa: typing.Callable[[], T_Result],
        antarctica: typing.Callable[[], T_Result],
        asia: typing.Callable[[], T_Result],
        europe: typing.Callable[[], T_Result],
        north_america: typing.Callable[[], T_Result],
        oceania: typing.Callable[[], T_Result],
        south_america: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LocationContinent.AFRICA:
            return africa()
        if self is LocationContinent.ANTARCTICA:
            return antarctica()
        if self is LocationContinent.ASIA:
            return asia()
        if self is LocationContinent.EUROPE:
            return europe()
        if self is LocationContinent.NORTH_AMERICA:
            return north_america()
        if self is LocationContinent.OCEANIA:
            return oceania()
        if self is LocationContinent.SOUTH_AMERICA:
            return south_america()
