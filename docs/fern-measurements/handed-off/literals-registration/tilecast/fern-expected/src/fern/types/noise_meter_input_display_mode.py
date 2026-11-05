

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoiseMeterInputDisplayMode(enum.StrEnum):
    OVERLAY = "overlay"
    PUSH = "push"

    def visit(self, overlay: typing.Callable[[], T_Result], push: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoiseMeterInputDisplayMode.OVERLAY:
            return overlay()
        if self is NoiseMeterInputDisplayMode.PUSH:
            return push()
