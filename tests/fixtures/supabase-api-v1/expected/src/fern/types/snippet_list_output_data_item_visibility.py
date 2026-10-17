

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SnippetListOutputDataItemVisibility(enum.StrEnum):
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
        if self is SnippetListOutputDataItemVisibility.USER:
            return user()
        if self is SnippetListOutputDataItemVisibility.PROJECT:
            return project()
        if self is SnippetListOutputDataItemVisibility.ORG:
            return org()
        if self is SnippetListOutputDataItemVisibility.PUBLIC:
            return public()
