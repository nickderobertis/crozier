

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClusteringZero(enum.StrEnum):
    """
    Exhaustive vector search, no clustering/ANN.
    """

    NONE = "None"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClusteringZero.NONE:
            return none()
