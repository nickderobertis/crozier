

import typing

from .block_message_action import BlockMessageAction
from .flag_to_channel_action import FlagToChannelAction
from .quarantine_user_action import QuarantineUserAction
from .user_communication_disabled_action import UserCommunicationDisabledAction

MlSpamUpsertRequestPartialActionsItem = typing.Union[
    BlockMessageAction, FlagToChannelAction, QuarantineUserAction, UserCommunicationDisabledAction
]
