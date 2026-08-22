

import typing

from .transaction_receipt_response import TransactionReceiptResponse

ReceiptProofsMap = typing.Dict[str, TransactionReceiptResponse]
"""
Key is tx hash, value is TransactionReceiptResponse
"""
