

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .sticker_format_types import StickerFormatTypes


class StandardStickerResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    tags: str
    type: int
    format_type: typing.Optional[StickerFormatTypes] = None
    description: typing.Optional[str] = None
    pack_id: SnowflakeType
    sort_value: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
