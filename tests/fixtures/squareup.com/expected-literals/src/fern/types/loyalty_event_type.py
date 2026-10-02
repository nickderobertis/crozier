

import typing

LoyaltyEventType = typing.Union[
    typing.Literal[
        "ACCUMULATE_POINTS",
        "CREATE_REWARD",
        "REDEEM_REWARD",
        "DELETE_REWARD",
        "ADJUST_POINTS",
        "EXPIRE_POINTS",
        "OTHER",
    ],
    typing.Any,
]
