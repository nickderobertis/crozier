

import typing

ConditionalActionType = typing.Union[
    typing.Literal[
        "JUMP_TO_PAGE", "CALCULATE", "REQUIRE_ANSWER", "SHOW_BLOCKS", "HIDE_BLOCKS", "HIDE_BUTTON_TO_DISABLE_COMPLETION"
    ],
    typing.Any,
]
