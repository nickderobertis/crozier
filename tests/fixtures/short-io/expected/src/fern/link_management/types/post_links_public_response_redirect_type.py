

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinksPublicResponseRedirectType(enum.StrEnum):
    """
    HTTP code for redirect
    """

    THREE_HUNDRED_ONE = "301"
    THREE_HUNDRED_TWO = "302"
    THREE_HUNDRED_SEVEN = "307"
    THREE_HUNDRED_EIGHT = "308"

    def visit(
        self,
        three_hundred_one: typing.Callable[[], T_Result],
        three_hundred_two: typing.Callable[[], T_Result],
        three_hundred_seven: typing.Callable[[], T_Result],
        three_hundred_eight: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostLinksPublicResponseRedirectType.THREE_HUNDRED_ONE:
            return three_hundred_one()
        if self is PostLinksPublicResponseRedirectType.THREE_HUNDRED_TWO:
            return three_hundred_two()
        if self is PostLinksPublicResponseRedirectType.THREE_HUNDRED_SEVEN:
            return three_hundred_seven()
        if self is PostLinksPublicResponseRedirectType.THREE_HUNDRED_EIGHT:
            return three_hundred_eight()
