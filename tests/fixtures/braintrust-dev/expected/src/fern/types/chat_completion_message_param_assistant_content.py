

import typing

from .chat_completion_content_part_text import ChatCompletionContentPartText

ChatCompletionMessageParamAssistantContent = typing.Union[str, typing.List[ChatCompletionContentPartText]]
