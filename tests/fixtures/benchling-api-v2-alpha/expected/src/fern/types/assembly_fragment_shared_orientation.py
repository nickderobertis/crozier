

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblyFragmentSharedOrientation(enum.StrEnum):
    FORWARD = "FORWARD"
    REVERSE = "REVERSE"

    def visit(self, forward: typing.Callable[[], T_Result], reverse: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssemblyFragmentSharedOrientation.FORWARD:
            return forward()
        if self is AssemblyFragmentSharedOrientation.REVERSE:
            return reverse()
