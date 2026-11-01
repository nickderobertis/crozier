

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdatePageMarkdownRequestType(enum.StrEnum):
    """
    The kind of edit to apply. Prefer `replace_content` (overwrite the whole page) or `update_content` (targeted find-and-replace). `insert_content` and `replace_content_range` are deprecated.
    """

    REPLACE_CONTENT = "replace_content"
    UPDATE_CONTENT = "update_content"
    INSERT_CONTENT = "insert_content"
    REPLACE_CONTENT_RANGE = "replace_content_range"

    def visit(
        self,
        replace_content: typing.Callable[[], T_Result],
        update_content: typing.Callable[[], T_Result],
        insert_content: typing.Callable[[], T_Result],
        replace_content_range: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdatePageMarkdownRequestType.REPLACE_CONTENT:
            return replace_content()
        if self is UpdatePageMarkdownRequestType.UPDATE_CONTENT:
            return update_content()
        if self is UpdatePageMarkdownRequestType.INSERT_CONTENT:
            return insert_content()
        if self is UpdatePageMarkdownRequestType.REPLACE_CONTENT_RANGE:
            return replace_content_range()
