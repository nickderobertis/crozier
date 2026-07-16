

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostPublishTypeRequestAction(enum.StrEnum):
    PUBLISH_TYPE = "PublishType"

    def visit(self, publish_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostPublishTypeRequestAction.PUBLISH_TYPE:
            return publish_type()
