

import typing

TitlerConflictErrorError = typing.Union[
    typing.Literal["title_is_manual", "title_in_flight", "title_state_changed"], typing.Any
]
