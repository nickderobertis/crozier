

import typing

from .tool_call import ToolCall
from .tool_call_delta import ToolCallDelta

ToolCallMessageToolCall = typing.Union[ToolCall, ToolCallDelta]
