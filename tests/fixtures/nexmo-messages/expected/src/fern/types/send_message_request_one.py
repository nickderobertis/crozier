

import typing

from .send_message_request_one_one import SendMessageRequestOneOne
from .send_message_request_one_three import SendMessageRequestOneThree
from .send_message_request_one_two import SendMessageRequestOneTwo
from .send_message_request_one_zero import SendMessageRequestOneZero

SendMessageRequestOne = typing.Union[
    SendMessageRequestOneZero, SendMessageRequestOneOne, SendMessageRequestOneTwo, SendMessageRequestOneThree
]
