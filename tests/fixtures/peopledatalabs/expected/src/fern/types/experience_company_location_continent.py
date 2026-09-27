

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExperienceCompanyLocationContinent(enum.StrEnum):
    """
    The continent associated with the company HQ
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
        if self is ExperienceCompanyLocationContinent.AFRICA:
            return africa()
        if self is ExperienceCompanyLocationContinent.ANTARCTICA:
            return antarctica()
        if self is ExperienceCompanyLocationContinent.ASIA:
            return asia()
        if self is ExperienceCompanyLocationContinent.EUROPE:
            return europe()
        if self is ExperienceCompanyLocationContinent.NORTH_AMERICA:
            return north_america()
        if self is ExperienceCompanyLocationContinent.OCEANIA:
            return oceania()
        if self is ExperienceCompanyLocationContinent.SOUTH_AMERICA:
            return south_america()
