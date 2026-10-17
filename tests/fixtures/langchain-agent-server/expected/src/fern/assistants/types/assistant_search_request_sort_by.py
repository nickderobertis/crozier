

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantSearchRequestSortBy(enum.StrEnum):
    """
    The field to sort by.
    """

    ASSISTANT_ID = "assistant_id"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    NAME = "name"
    GRAPH_ID = "graph_id"

    def visit(
        self,
        assistant_id: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        graph_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssistantSearchRequestSortBy.ASSISTANT_ID:
            return assistant_id()
        if self is AssistantSearchRequestSortBy.CREATED_AT:
            return created_at()
        if self is AssistantSearchRequestSortBy.UPDATED_AT:
            return updated_at()
        if self is AssistantSearchRequestSortBy.NAME:
            return name()
        if self is AssistantSearchRequestSortBy.GRAPH_ID:
            return graph_id()
