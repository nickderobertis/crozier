

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RecordsListAllRequestSortField(enum.StrEnum):
    AGREEMENT_DATE = "agreementDate"
    NAME = "name"
    LAST_UPDATED = "lastUpdated"

    def visit(
        self,
        agreement_date: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RecordsListAllRequestSortField.AGREEMENT_DATE:
            return agreement_date()
        if self is RecordsListAllRequestSortField.NAME:
            return name()
        if self is RecordsListAllRequestSortField.LAST_UPDATED:
            return last_updated()
