

import typing

from .tool_call import ToolCall
from .tool_call_delta import ToolCallDelta

ToolCallMessageToolCalls = typing.Union[typing.List[ToolCall], ToolCallDelta]
