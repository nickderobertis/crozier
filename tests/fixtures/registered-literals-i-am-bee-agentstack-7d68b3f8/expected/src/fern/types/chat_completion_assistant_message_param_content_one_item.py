

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionAssistantMessageParamContentOneItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionAssistantMessageParamContentOneItem_Refusal(UniversalBaseModel):
    type: typing.Literal["refusal"] = "refusal"
    refusal: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionAssistantMessageParamContentOneItem = typing_extensions.Annotated[
    typing.Union[
        ChatCompletionAssistantMessageParamContentOneItem_Text,
        ChatCompletionAssistantMessageParamContentOneItem_Refusal,
    ],
    pydantic.Field(discriminator="type"),
]
