

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SnippetResponseOutputVisibility(enum.StrEnum):
    USER = "user"
    PROJECT = "project"
    ORG = "org"
    PUBLIC = "public"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        org: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SnippetResponseOutputVisibility.USER:
            return user()
        if self is SnippetResponseOutputVisibility.PROJECT:
            return project()
        if self is SnippetResponseOutputVisibility.ORG:
            return org()
        if self is SnippetResponseOutputVisibility.PUBLIC:
            return public()
