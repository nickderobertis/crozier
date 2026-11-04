

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesIdentifiersListResponseItemAttributesCategory(enum.StrEnum):
    """
    The category of the identifier
    """

    ARK = "ark"
    DOI = "doi"

    def visit(self, ark: typing.Callable[[], T_Result], doi: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodesIdentifiersListResponseItemAttributesCategory.ARK:
            return ark()
        if self is NodesIdentifiersListResponseItemAttributesCategory.DOI:
            return doi()
