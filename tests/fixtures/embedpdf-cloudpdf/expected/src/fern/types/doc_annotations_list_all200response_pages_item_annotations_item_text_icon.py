

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon(enum.StrEnum):
    COMMENT = "comment"
    KEY = "key"
    NOTE = "note"
    HELP = "help"
    NEW_PARAGRAPH = "new-paragraph"
    PARAGRAPH = "paragraph"
    INSERT = "insert"

    def visit(
        self,
        comment: typing.Callable[[], T_Result],
        key: typing.Callable[[], T_Result],
        note: typing.Callable[[], T_Result],
        help: typing.Callable[[], T_Result],
        new_paragraph: typing.Callable[[], T_Result],
        paragraph: typing.Callable[[], T_Result],
        insert: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon.COMMENT:
            return comment()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon.KEY:
            return key()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon.NOTE:
            return note()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon.HELP:
            return help()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon.NEW_PARAGRAPH:
            return new_paragraph()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon.PARAGRAPH:
            return paragraph()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon.INSERT:
            return insert()
