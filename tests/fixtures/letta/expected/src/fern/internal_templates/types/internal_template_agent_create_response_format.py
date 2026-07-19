

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InternalTemplateAgentCreateResponseFormat_JsonObject(UniversalBaseModel):
    type: typing.Literal["json_object"] = "json_object"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateResponseFormat_JsonSchema(UniversalBaseModel):
    type: typing.Literal["json_schema"] = "json_schema"
    json_schema: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateResponseFormat_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InternalTemplateAgentCreateResponseFormat = typing_extensions.Annotated[
    typing.Union[
        InternalTemplateAgentCreateResponseFormat_JsonObject,
        InternalTemplateAgentCreateResponseFormat_JsonSchema,
        InternalTemplateAgentCreateResponseFormat_Text,
    ],
    pydantic.Field(discriminator="type"),
]
