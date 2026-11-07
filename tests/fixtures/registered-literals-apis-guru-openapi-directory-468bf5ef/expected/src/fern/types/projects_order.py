

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectsOrder(enum.StrEnum):
    """
    An enumeration.
    """

    ID = "id"
    NAME = "name"
    SUBTITLE = "subtitle"
    FIRST_UPDATED = "firstUpdated"
    LAST_UPDATED = "lastUpdated"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        subtitle: typing.Callable[[], T_Result],
        first_updated: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectsOrder.ID:
            return id()
        if self is ProjectsOrder.NAME:
            return name()
        if self is ProjectsOrder.SUBTITLE:
            return subtitle()
        if self is ProjectsOrder.FIRST_UPDATED:
            return first_updated()
        if self is ProjectsOrder.LAST_UPDATED:
            return last_updated()
