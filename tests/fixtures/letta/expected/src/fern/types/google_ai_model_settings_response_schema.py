

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleAiModelSettingsResponseSchema_JsonObject(UniversalBaseModel):
    type: typing.Literal["json_object"] = "json_object"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GoogleAiModelSettingsResponseSchema_JsonSchema(UniversalBaseModel):
    type: typing.Literal["json_schema"] = "json_schema"
    json_schema: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GoogleAiModelSettingsResponseSchema_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GoogleAiModelSettingsResponseSchema = typing_extensions.Annotated[
    typing.Union[
        GoogleAiModelSettingsResponseSchema_JsonObject,
        GoogleAiModelSettingsResponseSchema_JsonSchema,
        GoogleAiModelSettingsResponseSchema_Text,
    ],
    pydantic.Field(discriminator="type"),
]
