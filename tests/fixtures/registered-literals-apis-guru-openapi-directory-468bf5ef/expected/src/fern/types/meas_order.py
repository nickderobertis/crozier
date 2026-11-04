

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeasOrder(enum.StrEnum):
    """
    An enumeration.
    """

    CITY = "city"
    COUNTRY = "country"
    LOCATION = "location"
    DATETIME = "datetime"

    def visit(
        self,
        city: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasOrder.CITY:
            return city()
        if self is MeasOrder.COUNTRY:
            return country()
        if self is MeasOrder.LOCATION:
            return location()
        if self is MeasOrder.DATETIME:
            return datetime()
