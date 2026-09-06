

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .button_style_types import ButtonStyleTypes
from .component_emoji_response import ComponentEmojiResponse
from .snowflake_type import SnowflakeType


class ButtonComponentResponse(UniversalBaseModel):
    type: int
    id: int
    custom_id: typing.Optional[str] = None
    style: ButtonStyleTypes
    label: typing.Optional[str] = None
    disabled: typing.Optional[bool] = None
    emoji: typing.Optional[ComponentEmojiResponse] = None
    url: typing.Optional[str] = None
    sku_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
