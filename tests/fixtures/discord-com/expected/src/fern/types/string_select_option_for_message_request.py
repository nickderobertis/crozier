

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .component_emoji_for_message_request import ComponentEmojiForMessageRequest


class StringSelectOptionForMessageRequest(UniversalBaseModel):
    label: str
    value: str
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    emoji: typing.Optional[ComponentEmojiForMessageRequest] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
