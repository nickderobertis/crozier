

import typing

from .emails_send_request_reply_to_list_email import EmailsSendRequestReplyToListEmail
from .emails_send_request_reply_to_list_one_item import EmailsSendRequestReplyToListOneItem

EmailsSendRequestReplyToList = typing.Union[
    EmailsSendRequestReplyToListEmail, typing.List[EmailsSendRequestReplyToListOneItem]
]
