

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListAllRecordsRequestSortField(enum.StrEnum):
    AGREEMENT_DATE = "agreementDate"
    NAME = "name"
    LAST_UPDATED = "lastUpdated"

    def visit(
        self,
        agreement_date: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListAllRecordsRequestSortField.AGREEMENT_DATE:
            return agreement_date()
        if self is ListAllRecordsRequestSortField.NAME:
            return name()
        if self is ListAllRecordsRequestSortField.LAST_UPDATED:
            return last_updated()
