

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetPublishTypeRequestAction(str, enum.Enum):
    PUBLISH_TYPE = "PublishType"

    def visit(self, publish_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetPublishTypeRequestAction.PUBLISH_TYPE:
            return publish_type()
