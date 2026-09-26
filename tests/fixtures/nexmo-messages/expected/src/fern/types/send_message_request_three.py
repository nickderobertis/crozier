

import typing

from .send_message_request_three_four import SendMessageRequestThreeFour
from .send_message_request_three_one import SendMessageRequestThreeOne
from .send_message_request_three_three import SendMessageRequestThreeThree
from .send_message_request_three_two import SendMessageRequestThreeTwo
from .send_message_request_three_zero import SendMessageRequestThreeZero

SendMessageRequestThree = typing.Union[
    SendMessageRequestThreeZero,
    SendMessageRequestThreeOne,
    SendMessageRequestThreeTwo,
    SendMessageRequestThreeThree,
    SendMessageRequestThreeFour,
]
