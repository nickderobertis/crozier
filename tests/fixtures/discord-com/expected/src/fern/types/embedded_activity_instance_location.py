

import typing

from .guild_channel_location import GuildChannelLocation
from .private_channel_location import PrivateChannelLocation

EmbeddedActivityInstanceLocation = typing.Union[GuildChannelLocation, PrivateChannelLocation]
