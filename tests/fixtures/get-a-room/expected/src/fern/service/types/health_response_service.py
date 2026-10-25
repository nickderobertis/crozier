

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class HealthResponseService(enum.StrEnum):
    GET_A_ROOM = "get-a-room"

    def visit(self, get_a_room: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthResponseService.GET_A_ROOM:
            return get_a_room()
