

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationsOrder(enum.StrEnum):
    """
    An enumeration.
    """

    CITY = "city"
    COUNTRY = "country"
    LOCATION = "location"
    SOURCE_NAME = "sourceName"
    FIRST_UPDATED = "firstUpdated"
    LAST_UPDATED = "lastUpdated"
    COUNT = "count"
    RANDOM = "random"

    def visit(
        self,
        city: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        source_name: typing.Callable[[], T_Result],
        first_updated: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
        count: typing.Callable[[], T_Result],
        random: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LocationsOrder.CITY:
            return city()
        if self is LocationsOrder.COUNTRY:
            return country()
        if self is LocationsOrder.LOCATION:
            return location()
        if self is LocationsOrder.SOURCE_NAME:
            return source_name()
        if self is LocationsOrder.FIRST_UPDATED:
            return first_updated()
        if self is LocationsOrder.LAST_UPDATED:
            return last_updated()
        if self is LocationsOrder.COUNT:
            return count()
        if self is LocationsOrder.RANDOM:
            return random()
