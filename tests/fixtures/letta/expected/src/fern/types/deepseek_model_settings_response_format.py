

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeepseekModelSettingsResponseFormat_JsonObject(UniversalBaseModel):
    type: typing.Literal["json_object"] = "json_object"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DeepseekModelSettingsResponseFormat_JsonSchema(UniversalBaseModel):
    type: typing.Literal["json_schema"] = "json_schema"
    json_schema: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DeepseekModelSettingsResponseFormat_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DeepseekModelSettingsResponseFormat = typing_extensions.Annotated[
    typing.Union[
        DeepseekModelSettingsResponseFormat_JsonObject,
        DeepseekModelSettingsResponseFormat_JsonSchema,
        DeepseekModelSettingsResponseFormat_Text,
    ],
    pydantic.Field(discriminator="type"),
]
