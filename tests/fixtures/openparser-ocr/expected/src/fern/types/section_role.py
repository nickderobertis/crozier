

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SectionRole(enum.StrEnum):
    SECTION = "section"
    CHAPTER = "chapter"
    GROUP = "group"
    OTHER = "other"

    def visit(
        self,
        section: typing.Callable[[], T_Result],
        chapter: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SectionRole.SECTION:
            return section()
        if self is SectionRole.CHAPTER:
            return chapter()
        if self is SectionRole.GROUP:
            return group()
        if self is SectionRole.OTHER:
            return other()
