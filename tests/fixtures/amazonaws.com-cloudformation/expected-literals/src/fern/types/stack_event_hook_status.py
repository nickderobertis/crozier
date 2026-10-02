

import typing

StackEventHookStatus = typing.Union[
    typing.Literal["HOOK_IN_PROGRESS", "HOOK_COMPLETE_SUCCEEDED", "HOOK_COMPLETE_FAILED", "HOOK_FAILED"], typing.Any
]
