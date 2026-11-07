

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SourcesOrder(enum.StrEnum):
    """
    An enumeration.
    """

    SOURCE_NAME = "sourceName"
    FIRST_UPDATED = "firstUpdated"
    LAST_UPDATED = "lastUpdated"

    def visit(
        self,
        source_name: typing.Callable[[], T_Result],
        first_updated: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SourcesOrder.SOURCE_NAME:
            return source_name()
        if self is SourcesOrder.FIRST_UPDATED:
            return first_updated()
        if self is SourcesOrder.LAST_UPDATED:
            return last_updated()
