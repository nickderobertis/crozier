

import typing

from .chat_completion_content_part import ChatCompletionContentPart

ChatCompletionMessageParamUserContent = typing.Union[str, typing.List[ChatCompletionContentPart]]
