

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContentTemplateRequestKind(enum.StrEnum):
    POST = "post"
    REVIEW_REPLY = "review_reply"

    def visit(self, post: typing.Callable[[], T_Result], review_reply: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContentTemplateRequestKind.POST:
            return post()
        if self is ContentTemplateRequestKind.REVIEW_REPLY:
            return review_reply()
