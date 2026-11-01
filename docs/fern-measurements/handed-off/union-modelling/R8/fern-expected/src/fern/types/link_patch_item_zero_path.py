

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkPatchItemZeroPath(enum.StrEnum):
    """
    Which list of links.
    """

    RELATED = "/related"
    SEQUELS = "/sequels"

    def visit(self, related: typing.Callable[[], T_Result], sequels: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkPatchItemZeroPath.RELATED:
            return related()
        if self is LinkPatchItemZeroPath.SEQUELS:
            return sequels()
