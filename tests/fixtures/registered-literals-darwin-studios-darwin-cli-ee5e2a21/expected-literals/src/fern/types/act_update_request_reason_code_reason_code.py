

import typing

ActUpdateRequestReasonCodeReasonCode = typing.Union[
    typing.Literal[
        "PROMPT_INJECTION", "UNAUTHORIZED_ACTION", "DATA_EXPOSURE", "DECEPTIVE_COMPLETION", "COST_ABUSE", "OTHER"
    ],
    typing.Any,
]
