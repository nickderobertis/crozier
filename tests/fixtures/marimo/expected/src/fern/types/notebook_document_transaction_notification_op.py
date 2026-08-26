

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotebookDocumentTransactionNotificationOp(enum.StrEnum):
    NOTEBOOK_DOCUMENT_TRANSACTION = "notebook-document-transaction"

    def visit(self, notebook_document_transaction: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotebookDocumentTransactionNotificationOp.NOTEBOOK_DOCUMENT_TRANSACTION:
            return notebook_document_transaction()
