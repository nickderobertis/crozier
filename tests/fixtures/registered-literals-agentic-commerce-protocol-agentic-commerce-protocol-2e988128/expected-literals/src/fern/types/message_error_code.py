

import typing

MessageErrorCode = typing.Union[
    typing.Literal["missing", "invalid", "out_of_stock", "payment_declined", "requires_sign_in", "requires_3ds"],
    typing.Any,
]
