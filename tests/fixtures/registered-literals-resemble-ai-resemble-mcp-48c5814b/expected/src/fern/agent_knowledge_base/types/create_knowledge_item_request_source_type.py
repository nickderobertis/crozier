

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateKnowledgeItemRequestSourceType(enum.StrEnum):
    """
    Type of knowledge source
    """

    DOCUMENT = "document"
    URL = "url"
    TEXT = "text"

    def visit(
        self,
        document: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateKnowledgeItemRequestSourceType.DOCUMENT:
            return document()
        if self is CreateKnowledgeItemRequestSourceType.URL:
            return url()
        if self is CreateKnowledgeItemRequestSourceType.TEXT:
            return text()
