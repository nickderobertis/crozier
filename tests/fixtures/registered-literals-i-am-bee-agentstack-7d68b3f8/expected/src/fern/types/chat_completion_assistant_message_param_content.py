

import typing

from .chat_completion_assistant_message_param_content_one_item import ChatCompletionAssistantMessageParamContentOneItem

ChatCompletionAssistantMessageParamContent = typing.Union[
    str, typing.List[ChatCompletionAssistantMessageParamContentOneItem]
]
