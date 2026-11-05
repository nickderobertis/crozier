

import typing

DisplayControlActionType = typing.Union[
    typing.Literal[
        "display_power_on",
        "display_power_off",
        "display_set_input",
        "display_set_volume",
        "display_mute",
        "display_unmute",
        "display_set_brightness",
    ],
    typing.Any,
]
