

import typing

from .allowed_tools_param import AllowedToolsParam
from .specific_tool_choice_param import SpecificToolChoiceParam
from .tool_choice_value_enum import ToolChoiceValueEnum

CreateResponseBodyToolChoice = typing.Union[SpecificToolChoiceParam, ToolChoiceValueEnum, AllowedToolsParam]
