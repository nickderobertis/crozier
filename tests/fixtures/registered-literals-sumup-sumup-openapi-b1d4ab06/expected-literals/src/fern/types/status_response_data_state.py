

import typing

StatusResponseDataState = typing.Union[
    typing.Literal[
        "IDLE", "SELECTING_TIP", "WAITING_FOR_CARD", "WAITING_FOR_PIN", "WAITING_FOR_SIGNATURE", "UPDATING_FIRMWARE"
    ],
    typing.Any,
]
