

import typing

ChatMessagePolicyViolationDlpAction = typing.Union[
    typing.Literal["none", "notifySender", "blockAccess", "blockAccessExternal"], typing.Any
]
