

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .button_style_types import ButtonStyleTypes
from .component_emoji_for_message_request import ComponentEmojiForMessageRequest
from .snowflake_type import SnowflakeType


class ButtonComponentForMessageRequest(UniversalBaseModel):
    type: int
    custom_id: typing.Optional[str] = None
    style: ButtonStyleTypes
    label: typing.Optional[str] = None
    disabled: typing.Optional[bool] = None
    url: typing.Optional[str] = None
    sku_id: typing.Optional[SnowflakeType] = None
    emoji: typing.Optional[ComponentEmojiForMessageRequest] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
