

import typing

from .message_content_one_item_one import MessageContentOneItemOne
from .message_content_one_item_text import MessageContentOneItemText

MessageContentOneItem = typing.Union[MessageContentOneItemText, MessageContentOneItemOne]
