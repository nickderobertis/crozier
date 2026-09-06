

import typing

from .guild_channel_response import GuildChannelResponse
from .private_channel_response import PrivateChannelResponse
from .private_group_channel_response import PrivateGroupChannelResponse
from .thread_response import ThreadResponse

ResolvedObjectsResponseChannelsValue = typing.Union[
    GuildChannelResponse, PrivateChannelResponse, PrivateGroupChannelResponse, ThreadResponse
]
