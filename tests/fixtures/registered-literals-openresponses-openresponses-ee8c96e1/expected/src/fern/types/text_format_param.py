

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TextFormatParam_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TextFormatParam_JsonSchema(UniversalBaseModel):
    type: typing.Literal["json_schema"] = "json_schema"
    description: typing.Optional[str] = None
    name: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    strict: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TextFormatParam = typing_extensions.Annotated[
    typing.Union[TextFormatParam_Text, TextFormatParam_JsonSchema], pydantic.Field(discriminator="type")
]
