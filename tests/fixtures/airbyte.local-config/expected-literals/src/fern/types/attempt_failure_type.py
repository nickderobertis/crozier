

import typing

AttemptFailureType = typing.Union[
    typing.Literal["config_error", "system_error", "manual_cancellation", "refresh_schema"], typing.Any
]
