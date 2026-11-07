

import typing

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

ChatCompletionToolMessageParamContent = typing.Union[str, typing.List[ChatCompletionContentPartTextParam]]
