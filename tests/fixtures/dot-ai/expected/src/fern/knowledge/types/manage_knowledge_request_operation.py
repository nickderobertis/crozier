

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ManageKnowledgeRequestOperation(enum.StrEnum):
    """
    Operation to perform: "ingest" to add documents, "search" for semantic search, "deleteByUri" to remove all chunks for a document.
    """

    INGEST = "ingest"
    SEARCH = "search"
    DELETE_BY_URI = "deleteByUri"

    def visit(
        self,
        ingest: typing.Callable[[], T_Result],
        search: typing.Callable[[], T_Result],
        delete_by_uri: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ManageKnowledgeRequestOperation.INGEST:
            return ingest()
        if self is ManageKnowledgeRequestOperation.SEARCH:
            return search()
        if self is ManageKnowledgeRequestOperation.DELETE_BY_URI:
            return delete_by_uri()
