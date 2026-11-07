

import typing

from .allowed_tool_choice import AllowedToolChoice
from .function_tool_choice import FunctionToolChoice
from .tool_choice_value_enum import ToolChoiceValueEnum

ResponseFailedStreamingEventResponseToolChoice = typing.Union[
    FunctionToolChoice, ToolChoiceValueEnum, AllowedToolChoice
]
