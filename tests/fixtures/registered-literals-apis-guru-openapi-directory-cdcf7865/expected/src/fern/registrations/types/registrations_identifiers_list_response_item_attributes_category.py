

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RegistrationsIdentifiersListResponseItemAttributesCategory(enum.StrEnum):
    """
    The category of the identifier
    """

    ARK = "ark"
    DOI = "doi"

    def visit(self, ark: typing.Callable[[], T_Result], doi: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegistrationsIdentifiersListResponseItemAttributesCategory.ARK:
            return ark()
        if self is RegistrationsIdentifiersListResponseItemAttributesCategory.DOI:
            return doi()
