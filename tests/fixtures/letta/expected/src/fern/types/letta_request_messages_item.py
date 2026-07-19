

import typing

from .approval_create import ApprovalCreate
from .message_create import MessageCreate

LettaRequestMessagesItem = typing.Union[MessageCreate, ApprovalCreate]
