

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Spatial(enum.StrEnum):
    """
    An enumeration.
    """

    COUNTRY = "country"
    LOCATION = "location"
    PROJECT = "project"
    TOTAL = "total"

    def visit(
        self,
        country: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        total: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Spatial.COUNTRY:
            return country()
        if self is Spatial.LOCATION:
            return location()
        if self is Spatial.PROJECT:
            return project()
        if self is Spatial.TOTAL:
            return total()
