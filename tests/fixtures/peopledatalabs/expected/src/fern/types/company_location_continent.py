

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompanyLocationContinent(enum.StrEnum):
    """
    The company's current HQ continent
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
        if self is CompanyLocationContinent.AFRICA:
            return africa()
        if self is CompanyLocationContinent.ANTARCTICA:
            return antarctica()
        if self is CompanyLocationContinent.ASIA:
            return asia()
        if self is CompanyLocationContinent.EUROPE:
            return europe()
        if self is CompanyLocationContinent.NORTH_AMERICA:
            return north_america()
        if self is CompanyLocationContinent.OCEANIA:
            return oceania()
        if self is CompanyLocationContinent.SOUTH_AMERICA:
            return south_america()
