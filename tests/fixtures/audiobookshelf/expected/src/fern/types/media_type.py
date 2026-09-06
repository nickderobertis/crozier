

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MediaType(enum.StrEnum):
    """
    The type of media, will be book or podcast.
    """

    BOOK = "book"
    PODCAST = "podcast"

    def visit(self, book: typing.Callable[[], T_Result], podcast: typing.Callable[[], T_Result]) -> T_Result:
        if self is MediaType.BOOK:
            return book()
        if self is MediaType.PODCAST:
            return podcast()
