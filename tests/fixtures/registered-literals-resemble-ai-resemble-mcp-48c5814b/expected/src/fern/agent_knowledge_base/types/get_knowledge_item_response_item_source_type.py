

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetKnowledgeItemResponseItemSourceType(enum.StrEnum):
    DOCUMENT = "document"
    URL = "url"
    TEXT = "text"

    def visit(
        self,
        document: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetKnowledgeItemResponseItemSourceType.DOCUMENT:
            return document()
        if self is GetKnowledgeItemResponseItemSourceType.URL:
            return url()
        if self is GetKnowledgeItemResponseItemSourceType.TEXT:
            return text()
