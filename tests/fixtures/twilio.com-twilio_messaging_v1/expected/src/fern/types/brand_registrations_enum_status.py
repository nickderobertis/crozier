

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrandRegistrationsEnumStatus(enum.StrEnum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    IN_REVIEW = "IN_REVIEW"
    DELETED = "DELETED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        in_review: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BrandRegistrationsEnumStatus.PENDING:
            return pending()
        if self is BrandRegistrationsEnumStatus.APPROVED:
            return approved()
        if self is BrandRegistrationsEnumStatus.FAILED:
            return failed()
        if self is BrandRegistrationsEnumStatus.IN_REVIEW:
            return in_review()
        if self is BrandRegistrationsEnumStatus.DELETED:
            return deleted()
