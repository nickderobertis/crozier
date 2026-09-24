

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MerchantCertListRequestSortBy(enum.StrEnum):
    """
    The field to sort results by: 'createdDate' or 'id'. Defaults to 'id'.
    """

    CREATED_DATE = "createdDate"
    ID = "id"

    def visit(self, created_date: typing.Callable[[], T_Result], id: typing.Callable[[], T_Result]) -> T_Result:
        if self is MerchantCertListRequestSortBy.CREATED_DATE:
            return created_date()
        if self is MerchantCertListRequestSortBy.ID:
            return id()
