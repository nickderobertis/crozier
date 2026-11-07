

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClusteringOne(enum.StrEnum):
    """
    The number of clusters is automatically determined depending on the number of vectors per level and shard.
    """

    AUTO = "Auto"

    def visit(self, auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClusteringOne.AUTO:
            return auto()
