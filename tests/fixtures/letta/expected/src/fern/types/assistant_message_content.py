

import typing

from .letta_assistant_message_content_union import LettaAssistantMessageContentUnion

AssistantMessageContent = typing.Union[typing.List[LettaAssistantMessageContentUnion], str]
