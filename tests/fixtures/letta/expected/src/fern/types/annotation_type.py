

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnnotationType(enum.StrEnum):
    URL_CITATION = "url_citation"

    def visit(self, url_citation: typing.Callable[[], T_Result]) -> T_Result:
        if self is AnnotationType.URL_CITATION:
            return url_citation()
