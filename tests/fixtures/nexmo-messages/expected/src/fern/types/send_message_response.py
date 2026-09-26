

import typing

from .send_message_response_message_uuid import SendMessageResponseMessageUuid
from .send_message_response_one import SendMessageResponseOne
from .send_message_response_three import SendMessageResponseThree
from .send_message_response_two import SendMessageResponseTwo
from .send_message_response_zero import SendMessageResponseZero

SendMessageResponse = typing.Union[
    SendMessageResponseZero,
    SendMessageResponseOne,
    SendMessageResponseTwo,
    SendMessageResponseThree,
    SendMessageResponseMessageUuid,
]
