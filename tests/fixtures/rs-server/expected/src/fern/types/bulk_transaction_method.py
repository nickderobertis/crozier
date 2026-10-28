

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BulkTransactionMethod(enum.StrEnum):
    """
    Bulk Transaction Methods.
    """

    INSERT = "insert"
    UPSERT = "upsert"

    def visit(self, insert: typing.Callable[[], T_Result], upsert: typing.Callable[[], T_Result]) -> T_Result:
        if self is BulkTransactionMethod.INSERT:
            return insert()
        if self is BulkTransactionMethod.UPSERT:
            return upsert()
