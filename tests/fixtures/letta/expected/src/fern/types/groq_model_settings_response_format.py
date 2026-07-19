

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GroqModelSettingsResponseFormat_JsonObject(UniversalBaseModel):
    type: typing.Literal["json_object"] = "json_object"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GroqModelSettingsResponseFormat_JsonSchema(UniversalBaseModel):
    type: typing.Literal["json_schema"] = "json_schema"
    json_schema: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GroqModelSettingsResponseFormat_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GroqModelSettingsResponseFormat = typing_extensions.Annotated[
    typing.Union[
        GroqModelSettingsResponseFormat_JsonObject,
        GroqModelSettingsResponseFormat_JsonSchema,
        GroqModelSettingsResponseFormat_Text,
    ],
    pydantic.Field(discriminator="type"),
]
