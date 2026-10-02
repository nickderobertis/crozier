

import typing

BookingStatus = typing.Union[
    typing.Literal["PENDING", "CANCELLED_BY_CUSTOMER", "CANCELLED_BY_SELLER", "DECLINED", "ACCEPTED", "NO_SHOW"],
    typing.Any,
]
