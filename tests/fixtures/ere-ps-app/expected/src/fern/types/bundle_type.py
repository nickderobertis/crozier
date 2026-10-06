

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BundleType(enum.StrEnum):
    DOCUMENT = "DOCUMENT"
    MESSAGE = "MESSAGE"
    TRANSACTION = "TRANSACTION"
    TRANSACTIONRESPONSE = "TRANSACTIONRESPONSE"
    BATCH = "BATCH"
    BATCHRESPONSE = "BATCHRESPONSE"
    HISTORY = "HISTORY"
    SEARCHSET = "SEARCHSET"
    COLLECTION = "COLLECTION"
    NULL = "NULL"

    def visit(
        self,
        document: typing.Callable[[], T_Result],
        message: typing.Callable[[], T_Result],
        transaction: typing.Callable[[], T_Result],
        transactionresponse: typing.Callable[[], T_Result],
        batch: typing.Callable[[], T_Result],
        batchresponse: typing.Callable[[], T_Result],
        history: typing.Callable[[], T_Result],
        searchset: typing.Callable[[], T_Result],
        collection: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BundleType.DOCUMENT:
            return document()
        if self is BundleType.MESSAGE:
            return message()
        if self is BundleType.TRANSACTION:
            return transaction()
        if self is BundleType.TRANSACTIONRESPONSE:
            return transactionresponse()
        if self is BundleType.BATCH:
            return batch()
        if self is BundleType.BATCHRESPONSE:
            return batchresponse()
        if self is BundleType.HISTORY:
            return history()
        if self is BundleType.SEARCHSET:
            return searchset()
        if self is BundleType.COLLECTION:
            return collection()
        if self is BundleType.NULL:
            return null()
