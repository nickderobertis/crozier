

import typing

from .chat_completion_content_part_text import ChatCompletionContentPartText

ChatCompletionMessageParamSystemContent = typing.Union[str, typing.List[ChatCompletionContentPartText]]
