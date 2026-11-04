

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListKnowledgeItemsRequestSourceType(enum.StrEnum):
    DOCUMENT = "document"
    URL = "url"
    TEXT = "text"

    def visit(
        self,
        document: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListKnowledgeItemsRequestSourceType.DOCUMENT:
            return document()
        if self is ListKnowledgeItemsRequestSourceType.URL:
            return url()
        if self is ListKnowledgeItemsRequestSourceType.TEXT:
            return text()
