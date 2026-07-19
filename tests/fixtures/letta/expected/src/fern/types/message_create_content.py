

import typing

from .letta_message_content_union import LettaMessageContentUnion

MessageCreateContent = typing.Union[typing.List[LettaMessageContentUnion], str]
