

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTagsRequestInclude(enum.StrEnum):
    SERIES = "SERIES"
    BOOK = "BOOK"
    BOTH = "BOTH"

    def visit(
        self,
        series: typing.Callable[[], T_Result],
        book: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTagsRequestInclude.SERIES:
            return series()
        if self is GetTagsRequestInclude.BOOK:
            return book()
        if self is GetTagsRequestInclude.BOTH:
            return both()
