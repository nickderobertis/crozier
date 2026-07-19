

import typing

from .approval_create import ApprovalCreate
from .message_create import MessageCreate

LettaStreamingRequestMessagesItem = typing.Union[MessageCreate, ApprovalCreate]
