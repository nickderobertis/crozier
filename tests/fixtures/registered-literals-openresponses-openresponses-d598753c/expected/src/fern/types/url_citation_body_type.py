

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UrlCitationBodyType(enum.StrEnum):
    """
    The type of the URL citation. Always `url_citation`.
    """

    URL_CITATION = "url_citation"

    def visit(self, url_citation: typing.Callable[[], T_Result]) -> T_Result:
        if self is UrlCitationBodyType.URL_CITATION:
            return url_citation()
