

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CitiesOrder(enum.StrEnum):
    """
    An enumeration.
    """

    CITY = "city"
    COUNTRY = "country"
    FIRST_UPDATED = "firstUpdated"
    LAST_UPDATED = "lastUpdated"

    def visit(
        self,
        city: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
        first_updated: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CitiesOrder.CITY:
            return city()
        if self is CitiesOrder.COUNTRY:
            return country()
        if self is CitiesOrder.FIRST_UPDATED:
            return first_updated()
        if self is CitiesOrder.LAST_UPDATED:
            return last_updated()
