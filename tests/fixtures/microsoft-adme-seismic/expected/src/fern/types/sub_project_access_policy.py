

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubProjectAccessPolicy(enum.StrEnum):
    """
    Access policy for the subproject.
    """

    UNIFORM = "uniform"
    DATASET = "dataset"

    def visit(self, uniform: typing.Callable[[], T_Result], dataset: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubProjectAccessPolicy.UNIFORM:
            return uniform()
        if self is SubProjectAccessPolicy.DATASET:
            return dataset()
