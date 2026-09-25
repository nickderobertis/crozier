

import typing

from .send_message_request_two_five import SendMessageRequestTwoFive
from .send_message_request_two_four import SendMessageRequestTwoFour
from .send_message_request_two_one import SendMessageRequestTwoOne
from .send_message_request_two_seven import SendMessageRequestTwoSeven
from .send_message_request_two_six import SendMessageRequestTwoSix
from .send_message_request_two_three import SendMessageRequestTwoThree
from .send_message_request_two_two import SendMessageRequestTwoTwo
from .send_message_request_two_zero import SendMessageRequestTwoZero

SendMessageRequestTwo = typing.Union[
    SendMessageRequestTwoZero,
    SendMessageRequestTwoOne,
    SendMessageRequestTwoTwo,
    SendMessageRequestTwoThree,
    SendMessageRequestTwoFour,
    SendMessageRequestTwoFive,
    SendMessageRequestTwoSix,
    SendMessageRequestTwoSeven,
]
