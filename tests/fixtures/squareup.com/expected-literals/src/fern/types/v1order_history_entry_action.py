

import typing

V1OrderHistoryEntryAction = typing.Union[
    typing.Literal["ORDER_PLACED", "DECLINED", "PAYMENT_RECEIVED", "CANCELED", "COMPLETED", "REFUNDED", "EXPIRED"],
    typing.Any,
]
