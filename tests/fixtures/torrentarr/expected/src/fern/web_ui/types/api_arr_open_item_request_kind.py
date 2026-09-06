

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApiArrOpenItemRequestKind(enum.StrEnum):
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
        if self is ApiArrOpenItemRequestKind.MOVIE:
            return movie()
        if self is ApiArrOpenItemRequestKind.SERIES:
            return series()
        if self is ApiArrOpenItemRequestKind.ARTIST:
            return artist()
        if self is ApiArrOpenItemRequestKind.AUTHOR:
            return author()
