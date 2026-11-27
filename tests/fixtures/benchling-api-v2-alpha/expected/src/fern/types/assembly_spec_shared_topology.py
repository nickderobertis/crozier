

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblySpecSharedTopology(enum.StrEnum):
    """
    Whether the created constructs should be circular or linear.
    """

    CIRCULAR = "CIRCULAR"
    LINEAR = "LINEAR"

    def visit(self, circular: typing.Callable[[], T_Result], linear: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssemblySpecSharedTopology.CIRCULAR:
            return circular()
        if self is AssemblySpecSharedTopology.LINEAR:
            return linear()
