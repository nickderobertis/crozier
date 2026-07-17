

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetPublishTypeRequestAction(enum.StrEnum):
    PUBLISH_TYPE = "PublishType"

    def visit(self, publish_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetPublishTypeRequestAction.PUBLISH_TYPE:
            return publish_type()
