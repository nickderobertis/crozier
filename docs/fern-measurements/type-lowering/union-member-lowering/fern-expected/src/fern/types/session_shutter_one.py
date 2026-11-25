

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionShutterOne(enum.StrEnum):
    FOCAL_PLANE = "focal-plane"

    def visit(self, focal_plane: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionShutterOne.FOCAL_PLANE:
            return focal_plane()
