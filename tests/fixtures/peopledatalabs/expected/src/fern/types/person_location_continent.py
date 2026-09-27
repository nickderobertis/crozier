

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PersonLocationContinent(enum.StrEnum):
    """
    the current continent of the person
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
        if self is PersonLocationContinent.AFRICA:
            return africa()
        if self is PersonLocationContinent.ANTARCTICA:
            return antarctica()
        if self is PersonLocationContinent.ASIA:
            return asia()
        if self is PersonLocationContinent.EUROPE:
            return europe()
        if self is PersonLocationContinent.NORTH_AMERICA:
            return north_america()
        if self is PersonLocationContinent.OCEANIA:
            return oceania()
        if self is PersonLocationContinent.SOUTH_AMERICA:
            return south_america()
