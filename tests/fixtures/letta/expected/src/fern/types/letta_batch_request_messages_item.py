

import typing

from .approval_create import ApprovalCreate
from .message_create import MessageCreate

LettaBatchRequestMessagesItem = typing.Union[MessageCreate, ApprovalCreate]
