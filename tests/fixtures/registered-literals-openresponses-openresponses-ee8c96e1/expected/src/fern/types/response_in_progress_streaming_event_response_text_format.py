

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResponseInProgressStreamingEventResponseTextFormat_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseInProgressStreamingEventResponseTextFormat_JsonObject(UniversalBaseModel):
    type: typing.Literal["json_object"] = "json_object"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseInProgressStreamingEventResponseTextFormat_JsonSchema(UniversalBaseModel):
    type: typing.Literal["json_schema"] = "json_schema"
    name: str
    description: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    strict: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResponseInProgressStreamingEventResponseTextFormat = typing_extensions.Annotated[
    typing.Union[
        ResponseInProgressStreamingEventResponseTextFormat_Text,
        ResponseInProgressStreamingEventResponseTextFormat_JsonObject,
        ResponseInProgressStreamingEventResponseTextFormat_JsonSchema,
    ],
    pydantic.Field(discriminator="type"),
]
