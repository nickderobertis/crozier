

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRegisterPublisherRequestAction(enum.StrEnum):
    REGISTER_PUBLISHER = "RegisterPublisher"

    def visit(self, register_publisher: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRegisterPublisherRequestAction.REGISTER_PUBLISHER:
            return register_publisher()
