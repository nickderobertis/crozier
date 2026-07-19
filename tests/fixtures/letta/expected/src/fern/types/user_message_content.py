

import typing

from .letta_user_message_content_union import LettaUserMessageContentUnion

UserMessageContent = typing.Union[typing.List[LettaUserMessageContentUnion], str]
