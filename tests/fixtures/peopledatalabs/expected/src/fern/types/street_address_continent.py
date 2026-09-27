

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreetAddressContinent(enum.StrEnum):
    """
    The continent associated with the country in the location object
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
        if self is StreetAddressContinent.AFRICA:
            return africa()
        if self is StreetAddressContinent.ANTARCTICA:
            return antarctica()
        if self is StreetAddressContinent.ASIA:
            return asia()
        if self is StreetAddressContinent.EUROPE:
            return europe()
        if self is StreetAddressContinent.NORTH_AMERICA:
            return north_america()
        if self is StreetAddressContinent.OCEANIA:
            return oceania()
        if self is StreetAddressContinent.SOUTH_AMERICA:
            return south_america()
