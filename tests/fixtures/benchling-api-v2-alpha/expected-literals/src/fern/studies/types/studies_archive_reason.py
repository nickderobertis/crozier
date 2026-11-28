

import typing

StudiesArchiveReason = typing.Union[
    typing.Literal["Made in error", "Retired", "Expended", "Shipped", "Contaminated", "Expired", "Missing", "Other"],
    typing.Any,
]
