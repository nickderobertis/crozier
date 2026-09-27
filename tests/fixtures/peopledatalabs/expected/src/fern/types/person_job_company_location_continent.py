

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PersonJobCompanyLocationContinent(enum.StrEnum):
    """
    A person's current company's HQ continent
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
        if self is PersonJobCompanyLocationContinent.AFRICA:
            return africa()
        if self is PersonJobCompanyLocationContinent.ANTARCTICA:
            return antarctica()
        if self is PersonJobCompanyLocationContinent.ASIA:
            return asia()
        if self is PersonJobCompanyLocationContinent.EUROPE:
            return europe()
        if self is PersonJobCompanyLocationContinent.NORTH_AMERICA:
            return north_america()
        if self is PersonJobCompanyLocationContinent.OCEANIA:
            return oceania()
        if self is PersonJobCompanyLocationContinent.SOUTH_AMERICA:
            return south_america()
