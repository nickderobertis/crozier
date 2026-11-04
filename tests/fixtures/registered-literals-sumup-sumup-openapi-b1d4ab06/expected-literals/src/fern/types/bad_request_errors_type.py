

import typing

BadRequestErrorsType = typing.Union[
    typing.Literal["INVALID_BEARER_TOKEN", "INVALID_USER_AGENT", "NOT_ENOUGH_UNPAID_PAYOUTS", "DUPLICATE_HEADERS"],
    typing.Any,
]
