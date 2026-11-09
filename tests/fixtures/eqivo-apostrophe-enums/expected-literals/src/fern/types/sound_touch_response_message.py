

import typing

SoundTouchResponseMessage = typing.Union[
    typing.Literal[
        "SoundTouch Executed",
        "CallUUID Parameter Missing",
        "AudioDirection Parameter Must be 'in' or 'out'",
        "PitchSemiTones Parameter must be float",
        "PitchSemiTones Parameter must be between -14 and 14",
        "PitchOctaves Parameter must be float",
        "PitchOctaves Parameter must be between -1 and 1",
        "Pitch Parameter must be float",
        "Pitch Parameter must be > 0",
        "Rate Parameter must be float",
        "Rate Parameter must be > 0",
        "Tempo Parameter must be float",
        "Tempo Parameter must be > 0",
        "SoundTouch Failed -- Call not found",
        "SoundTouch Failed",
    ],
    typing.Any,
]
