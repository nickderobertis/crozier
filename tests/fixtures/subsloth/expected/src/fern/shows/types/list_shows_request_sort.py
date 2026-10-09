

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListShowsRequestSort(enum.StrEnum):
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
        if self is ListShowsRequestSort.PUBLICATION_DATE:
            return publication_date()
        if self is ListShowsRequestSort.POPULARITY:
            return popularity()
        if self is ListShowsRequestSort.RATING:
            return rating()
        if self is ListShowsRequestSort.NAME:
            return name()
        if self is ListShowsRequestSort.YEAR:
            return year()
