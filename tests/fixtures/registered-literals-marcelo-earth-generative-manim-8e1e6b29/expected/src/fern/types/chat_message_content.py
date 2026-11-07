

import typing

from .chat_message_content_one_item import ChatMessageContentOneItem

ChatMessageContent = typing.Union[str, typing.List[ChatMessageContentOneItem]]
