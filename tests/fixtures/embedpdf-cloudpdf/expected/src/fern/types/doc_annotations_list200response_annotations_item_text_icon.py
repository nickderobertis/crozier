

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemTextIcon(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemTextIcon.COMMENT:
            return comment()
        if self is DocAnnotationsList200ResponseAnnotationsItemTextIcon.KEY:
            return key()
        if self is DocAnnotationsList200ResponseAnnotationsItemTextIcon.NOTE:
            return note()
        if self is DocAnnotationsList200ResponseAnnotationsItemTextIcon.HELP:
            return help()
        if self is DocAnnotationsList200ResponseAnnotationsItemTextIcon.NEW_PARAGRAPH:
            return new_paragraph()
        if self is DocAnnotationsList200ResponseAnnotationsItemTextIcon.PARAGRAPH:
            return paragraph()
        if self is DocAnnotationsList200ResponseAnnotationsItemTextIcon.INSERT:
            return insert()
