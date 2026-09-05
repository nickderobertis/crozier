

import typing

from .friend_invite_response import FriendInviteResponse
from .group_dm_invite_response import GroupDmInviteResponse
from .guild_invite_response import GuildInviteResponse

CreateChannelInviteResponse = typing.Union[FriendInviteResponse, GroupDmInviteResponse, GuildInviteResponse]
