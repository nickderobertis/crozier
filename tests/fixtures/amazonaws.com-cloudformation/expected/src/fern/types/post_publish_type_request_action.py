

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPublishTypeRequestAction(str, enum.Enum):
    PUBLISH_TYPE = "PublishType"

    def visit(self, publish_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostPublishTypeRequestAction.PUBLISH_TYPE:
            return publish_type()
