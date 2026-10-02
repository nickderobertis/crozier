

import typing

CommandType = typing.Union[
    typing.Literal[
        "STOP_MOVEMENT",
        "MOVE_FORWARD",
        "MOVE_BACKWARD",
        "MOVE_TO",
        "CARGO_OPEN",
        "CARGO_CLOSE",
        "CARGO_LIFT",
        "CARGO_LOWER",
        "CARGO_CHECK_QR",
        "SCAN_LOCATION",
        "WAIT",
    ],
    typing.Any,
]
