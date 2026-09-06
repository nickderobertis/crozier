

import typing

from .guild_sticker_response import GuildStickerResponse
from .standard_sticker_response import StandardStickerResponse

BasicMessageResponseStickersItem = typing.Union[GuildStickerResponse, StandardStickerResponse]
