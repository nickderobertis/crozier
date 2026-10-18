

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantSearchRequestSelectItem(enum.StrEnum):
    ASSISTANT_ID = "assistant_id"
    GRAPH_ID = "graph_id"
    NAME = "name"
    DESCRIPTION = "description"
    CONFIG = "config"
    CONTEXT = "context"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    METADATA = "metadata"
    VERSION = "version"

    def visit(
        self,
        assistant_id: typing.Callable[[], T_Result],
        graph_id: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        description: typing.Callable[[], T_Result],
        config: typing.Callable[[], T_Result],
        context: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        metadata: typing.Callable[[], T_Result],
        version: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssistantSearchRequestSelectItem.ASSISTANT_ID:
            return assistant_id()
        if self is AssistantSearchRequestSelectItem.GRAPH_ID:
            return graph_id()
        if self is AssistantSearchRequestSelectItem.NAME:
            return name()
        if self is AssistantSearchRequestSelectItem.DESCRIPTION:
            return description()
        if self is AssistantSearchRequestSelectItem.CONFIG:
            return config()
        if self is AssistantSearchRequestSelectItem.CONTEXT:
            return context()
        if self is AssistantSearchRequestSelectItem.CREATED_AT:
            return created_at()
        if self is AssistantSearchRequestSelectItem.UPDATED_AT:
            return updated_at()
        if self is AssistantSearchRequestSelectItem.METADATA:
            return metadata()
        if self is AssistantSearchRequestSelectItem.VERSION:
            return version()
