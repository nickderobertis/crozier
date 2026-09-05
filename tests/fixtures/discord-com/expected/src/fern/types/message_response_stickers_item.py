

import typing

from .guild_sticker_response import GuildStickerResponse
from .standard_sticker_response import StandardStickerResponse

MessageResponseStickersItem = typing.Union[GuildStickerResponse, StandardStickerResponse]
