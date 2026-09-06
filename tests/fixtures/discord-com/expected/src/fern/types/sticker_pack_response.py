

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .standard_sticker_response import StandardStickerResponse


class StickerPackResponse(UniversalBaseModel):
    id: SnowflakeType
    sku_id: SnowflakeType
    name: str
    description: typing.Optional[str] = None
    stickers: typing.List[StandardStickerResponse]
    cover_sticker_id: typing.Optional[SnowflakeType] = None
    banner_asset_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
