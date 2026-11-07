

import typing

from .assistant_message_item_param import AssistantMessageItemParam
from .developer_message_item_param import DeveloperMessageItemParam
from .function_call_item_param import FunctionCallItemParam
from .function_call_output_item_param import FunctionCallOutputItemParam
from .item_reference_param import ItemReferenceParam
from .reasoning_item_param import ReasoningItemParam
from .system_message_item_param import SystemMessageItemParam
from .user_message_item_param import UserMessageItemParam

ItemParam = typing.Union[
    ItemReferenceParam,
    ReasoningItemParam,
    UserMessageItemParam,
    SystemMessageItemParam,
    DeveloperMessageItemParam,
    AssistantMessageItemParam,
    FunctionCallItemParam,
    FunctionCallOutputItemParam,
]
