

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SummaryType(enum.StrEnum):
    """
    The type of summary
    """

    BULLETS = "bullets"
    BULLETS_VERBOSE = "bullets_verbose"
    GIST = "gist"
    HEADLINE = "headline"
    PARAGRAPH = "paragraph"

    def visit(
        self,
        bullets: typing.Callable[[], T_Result],
        bullets_verbose: typing.Callable[[], T_Result],
        gist: typing.Callable[[], T_Result],
        headline: typing.Callable[[], T_Result],
        paragraph: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SummaryType.BULLETS:
            return bullets()
        if self is SummaryType.BULLETS_VERBOSE:
            return bullets_verbose()
        if self is SummaryType.GIST:
            return gist()
        if self is SummaryType.HEADLINE:
            return headline()
        if self is SummaryType.PARAGRAPH:
            return paragraph()
