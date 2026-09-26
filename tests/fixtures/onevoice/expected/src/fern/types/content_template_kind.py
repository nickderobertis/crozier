

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContentTemplateKind(enum.StrEnum):
    POST = "post"
    REVIEW_REPLY = "review_reply"

    def visit(self, post: typing.Callable[[], T_Result], review_reply: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContentTemplateKind.POST:
            return post()
        if self is ContentTemplateKind.REVIEW_REPLY:
            return review_reply()
