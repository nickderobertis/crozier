

import typing

from ...types.chat_completion_allowed_tool_choice_param import ChatCompletionAllowedToolChoiceParam
from ...types.chat_completion_named_tool_choice_custom_param import ChatCompletionNamedToolChoiceCustomParam
from ...types.chat_completion_named_tool_choice_param import ChatCompletionNamedToolChoiceParam
from .chat_completion_request_tool_choice_zero import ChatCompletionRequestToolChoiceZero

ChatCompletionRequestToolChoice = typing.Union[
    ChatCompletionRequestToolChoiceZero,
    ChatCompletionAllowedToolChoiceParam,
    ChatCompletionNamedToolChoiceParam,
    ChatCompletionNamedToolChoiceCustomParam,
]
