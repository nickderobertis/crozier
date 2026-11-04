

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListKnowledgeItemsResponseItemsItemSourceType(enum.StrEnum):
    DOCUMENT = "document"
    URL = "url"
    TEXT = "text"

    def visit(
        self,
        document: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListKnowledgeItemsResponseItemsItemSourceType.DOCUMENT:
            return document()
        if self is ListKnowledgeItemsResponseItemsItemSourceType.URL:
            return url()
        if self is ListKnowledgeItemsResponseItemsItemSourceType.TEXT:
            return text()
