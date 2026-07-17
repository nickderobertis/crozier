

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostListingsRequestExclusiveChannel(enum.StrEnum):
    """
    Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'
    """

    SELLER_SITE = "seller_site"
    REVERB = "reverb"
    NONE = "none"

    def visit(
        self,
        seller_site: typing.Callable[[], T_Result],
        reverb: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostListingsRequestExclusiveChannel.SELLER_SITE:
            return seller_site()
        if self is PostListingsRequestExclusiveChannel.REVERB:
            return reverb()
        if self is PostListingsRequestExclusiveChannel.NONE:
            return none()
