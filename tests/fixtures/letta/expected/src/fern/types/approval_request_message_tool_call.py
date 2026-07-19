

import typing

from .tool_call import ToolCall
from .tool_call_delta import ToolCallDelta

ApprovalRequestMessageToolCall = typing.Union[ToolCall, ToolCallDelta]
