

import typing

from .emails_send_request_bcc_one_item import EmailsSendRequestBccOneItem
from .emails_send_request_bcc_zero import EmailsSendRequestBccZero

EmailsSendRequestBcc = typing.Union[EmailsSendRequestBccZero, typing.List[EmailsSendRequestBccOneItem]]
