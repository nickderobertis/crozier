

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetRegisterPublisherRequestAction(str, enum.Enum):
    REGISTER_PUBLISHER = "RegisterPublisher"

    def visit(self, register_publisher: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRegisterPublisherRequestAction.REGISTER_PUBLISHER:
            return register_publisher()
