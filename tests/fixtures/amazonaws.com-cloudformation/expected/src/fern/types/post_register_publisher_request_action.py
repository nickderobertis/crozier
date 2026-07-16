

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostRegisterPublisherRequestAction(str, enum.Enum):
    REGISTER_PUBLISHER = "RegisterPublisher"

    def visit(self, register_publisher: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostRegisterPublisherRequestAction.REGISTER_PUBLISHER:
            return register_publisher()
