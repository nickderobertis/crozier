

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebArrOpenItemRequestKind(enum.StrEnum):
    MOVIE = "movie"
    SERIES = "series"
    ARTIST = "artist"
    AUTHOR = "author"

    def visit(
        self,
        movie: typing.Callable[[], T_Result],
        series: typing.Callable[[], T_Result],
        artist: typing.Callable[[], T_Result],
        author: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebArrOpenItemRequestKind.MOVIE:
            return movie()
        if self is WebArrOpenItemRequestKind.SERIES:
            return series()
        if self is WebArrOpenItemRequestKind.ARTIST:
            return artist()
        if self is WebArrOpenItemRequestKind.AUTHOR:
            return author()
