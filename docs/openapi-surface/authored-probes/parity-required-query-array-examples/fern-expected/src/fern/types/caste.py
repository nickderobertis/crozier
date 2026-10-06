

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Caste(enum.StrEnum):
    WORKER = "worker"
    DRONE = "drone"
    QUEEN = "queen"

    def visit(
        self,
        worker: typing.Callable[[], T_Result],
        drone: typing.Callable[[], T_Result],
        queen: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Caste.WORKER:
            return worker()
        if self is Caste.DRONE:
            return drone()
        if self is Caste.QUEEN:
            return queen()
