

import typing

from .private_channel_response import PrivateChannelResponse
from .private_group_channel_response import PrivateGroupChannelResponse

CreateDmResponse = typing.Union[PrivateChannelResponse, PrivateGroupChannelResponse]
