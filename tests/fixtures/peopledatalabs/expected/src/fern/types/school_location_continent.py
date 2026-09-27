

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchoolLocationContinent(enum.StrEnum):
    """
    The continent associated with the school
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
        if self is SchoolLocationContinent.AFRICA:
            return africa()
        if self is SchoolLocationContinent.ANTARCTICA:
            return antarctica()
        if self is SchoolLocationContinent.ASIA:
            return asia()
        if self is SchoolLocationContinent.EUROPE:
            return europe()
        if self is SchoolLocationContinent.NORTH_AMERICA:
            return north_america()
        if self is SchoolLocationContinent.OCEANIA:
            return oceania()
        if self is SchoolLocationContinent.SOUTH_AMERICA:
            return south_america()
