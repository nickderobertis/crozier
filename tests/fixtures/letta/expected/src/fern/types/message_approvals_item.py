

import typing

from .approval_return import ApprovalReturn
from .letta_schemas_message_tool_return_output import LettaSchemasMessageToolReturnOutput

MessageApprovalsItem = typing.Union[ApprovalReturn, LettaSchemasMessageToolReturnOutput]
