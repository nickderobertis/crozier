

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SavedSearchUpdateRequestUpdateMaskItem(enum.StrEnum):
    NAME = "name"
    DESCRIPTION = "description"
    QUERY = "query"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        description: typing.Callable[[], T_Result],
        query: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SavedSearchUpdateRequestUpdateMaskItem.NAME:
            return name()
        if self is SavedSearchUpdateRequestUpdateMaskItem.DESCRIPTION:
            return description()
        if self is SavedSearchUpdateRequestUpdateMaskItem.QUERY:
            return query()
