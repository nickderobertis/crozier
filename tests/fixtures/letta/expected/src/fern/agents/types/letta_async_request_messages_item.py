

import typing

from ...types.approval_create import ApprovalCreate
from ...types.message_create import MessageCreate

LettaAsyncRequestMessagesItem = typing.Union[MessageCreate, ApprovalCreate]
