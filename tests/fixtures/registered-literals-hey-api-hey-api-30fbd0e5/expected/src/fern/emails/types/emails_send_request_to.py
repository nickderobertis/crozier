

import typing

from .emails_send_request_to_one_item import EmailsSendRequestToOneItem
from .emails_send_request_to_zero import EmailsSendRequestToZero

EmailsSendRequestTo = typing.Union[EmailsSendRequestToZero, typing.List[EmailsSendRequestToOneItem]]
