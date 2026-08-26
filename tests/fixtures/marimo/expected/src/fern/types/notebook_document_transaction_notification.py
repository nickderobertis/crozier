

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notebook_document_transaction_notification_op import NotebookDocumentTransactionNotificationOp
from .transaction import Transaction


class NotebookDocumentTransactionNotification(UniversalBaseModel):
    """
    Broadcasts an applied transaction to the frontend.

        Sent by the session when the document changes (from any source).
        The frontend applies the ops to update its local state.
    """

    op: NotebookDocumentTransactionNotificationOp
    transaction: Transaction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
