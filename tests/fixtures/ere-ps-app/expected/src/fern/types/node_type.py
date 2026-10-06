

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeType(enum.StrEnum):
    ELEMENT = "Element"
    TEXT = "Text"
    COMMENT = "Comment"
    DOC_TYPE = "DocType"
    DOCUMENT = "Document"
    INSTRUCTION = "Instruction"

    def visit(
        self,
        element: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        comment: typing.Callable[[], T_Result],
        doc_type: typing.Callable[[], T_Result],
        document: typing.Callable[[], T_Result],
        instruction: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NodeType.ELEMENT:
            return element()
        if self is NodeType.TEXT:
            return text()
        if self is NodeType.COMMENT:
            return comment()
        if self is NodeType.DOC_TYPE:
            return doc_type()
        if self is NodeType.DOCUMENT:
            return document()
        if self is NodeType.INSTRUCTION:
            return instruction()
