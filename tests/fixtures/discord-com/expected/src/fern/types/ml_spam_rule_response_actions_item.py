

import typing

from .block_message_action_response import BlockMessageActionResponse
from .flag_to_channel_action_response import FlagToChannelActionResponse
from .quarantine_user_action_response import QuarantineUserActionResponse
from .user_communication_disabled_action_response import UserCommunicationDisabledActionResponse

MlSpamRuleResponseActionsItem = typing.Union[
    BlockMessageActionResponse,
    FlagToChannelActionResponse,
    QuarantineUserActionResponse,
    UserCommunicationDisabledActionResponse,
]
