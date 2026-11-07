

import typing

ThoughtType = typing.Union[
    typing.Literal["plan", "metadata", "user_goal_check", "internal_plan", "failure_describe", "termination"],
    typing.Any,
]
