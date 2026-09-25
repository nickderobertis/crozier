

import typing

from .send_message_request_four import SendMessageRequestFour
from .send_message_request_one import SendMessageRequestOne
from .send_message_request_three import SendMessageRequestThree
from .send_message_request_two import SendMessageRequestTwo
from .send_message_request_zero import SendMessageRequestZero

SendMessageRequest = typing.Union[
    SendMessageRequestZero,
    SendMessageRequestOne,
    SendMessageRequestTwo,
    SendMessageRequestThree,
    SendMessageRequestFour,
]
