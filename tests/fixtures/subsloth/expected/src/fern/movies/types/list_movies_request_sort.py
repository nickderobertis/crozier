

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListMoviesRequestSort(enum.StrEnum):
    PUBLICATION_DATE = "publication_date"
    POPULARITY = "popularity"
    RATING = "rating"
    NAME = "name"
    YEAR = "year"

    def visit(
        self,
        publication_date: typing.Callable[[], T_Result],
        popularity: typing.Callable[[], T_Result],
        rating: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListMoviesRequestSort.PUBLICATION_DATE:
            return publication_date()
        if self is ListMoviesRequestSort.POPULARITY:
            return popularity()
        if self is ListMoviesRequestSort.RATING:
            return rating()
        if self is ListMoviesRequestSort.NAME:
            return name()
        if self is ListMoviesRequestSort.YEAR:
            return year()
