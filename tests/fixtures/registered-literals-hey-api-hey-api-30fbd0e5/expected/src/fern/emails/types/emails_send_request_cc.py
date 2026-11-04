

import typing

from .emails_send_request_cc_one_item import EmailsSendRequestCcOneItem
from .emails_send_request_cc_zero import EmailsSendRequestCcZero

EmailsSendRequestCc = typing.Union[EmailsSendRequestCcZero, typing.List[EmailsSendRequestCcOneItem]]
