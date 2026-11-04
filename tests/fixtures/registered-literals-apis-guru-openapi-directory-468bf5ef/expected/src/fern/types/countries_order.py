

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CountriesOrder(enum.StrEnum):
    """
    An enumeration.
    """

    COUNTRY = "country"
    FIRST_UPDATED = "firstUpdated"
    LAST_UPDATED = "lastUpdated"
    LOCATIONS = "locations"
    COUNT = "count"

    def visit(
        self,
        country: typing.Callable[[], T_Result],
        first_updated: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
        locations: typing.Callable[[], T_Result],
        count: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CountriesOrder.COUNTRY:
            return country()
        if self is CountriesOrder.FIRST_UPDATED:
            return first_updated()
        if self is CountriesOrder.LAST_UPDATED:
            return last_updated()
        if self is CountriesOrder.LOCATIONS:
            return locations()
        if self is CountriesOrder.COUNT:
            return count()
