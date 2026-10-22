

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubProjectCreateBodyAccessPolicy(enum.StrEnum):
    """
    The datasets access level mode: "uniform" (uniform data access to all subprojects datasets) or "datasets" (acl can be applied at dataset level)
    """

    UNIFORM = "uniform"
    DATASET = "dataset"

    def visit(self, uniform: typing.Callable[[], T_Result], dataset: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubProjectCreateBodyAccessPolicy.UNIFORM:
            return uniform()
        if self is SubProjectCreateBodyAccessPolicy.DATASET:
            return dataset()
