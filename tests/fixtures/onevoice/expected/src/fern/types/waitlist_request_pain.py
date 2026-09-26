

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WaitlistRequestPain(enum.StrEnum):
    """
    Optional strongest-pain segment.
    """

    REVIEWS = "reviews"
    POSTS = "posts"
    CARD = "card"

    def visit(
        self,
        reviews: typing.Callable[[], T_Result],
        posts: typing.Callable[[], T_Result],
        card: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WaitlistRequestPain.REVIEWS:
            return reviews()
        if self is WaitlistRequestPain.POSTS:
            return posts()
        if self is WaitlistRequestPain.CARD:
            return card()
