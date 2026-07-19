

import typing

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

ChatCompletionSystemMessageParamContent = typing.Union[str, typing.List[ChatCompletionContentPartTextParam]]
