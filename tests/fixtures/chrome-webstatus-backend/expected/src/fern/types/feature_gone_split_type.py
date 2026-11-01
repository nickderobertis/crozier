

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FeatureGoneSplitType(enum.StrEnum):
    """
    Indicates the feature was removed due to a split.
    """

    SPLIT = "split"

    def visit(self, split: typing.Callable[[], T_Result]) -> T_Result:
        if self is FeatureGoneSplitType.SPLIT:
            return split()
