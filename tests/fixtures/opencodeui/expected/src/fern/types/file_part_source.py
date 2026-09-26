

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_part_source_text import FilePartSourceText
from .range import Range


class FilePartSource_File(UniversalBaseModel):
    type: typing.Literal["file"] = "file"
    text: FilePartSourceText
    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilePartSource_Symbol(UniversalBaseModel):
    type: typing.Literal["symbol"] = "symbol"
    text: FilePartSourceText
    path: str
    range: Range
    name: str
    kind: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilePartSource_Resource(UniversalBaseModel):
    type: typing.Literal["resource"] = "resource"
    text: FilePartSourceText
    client_name: typing_extensions.Annotated[str, FieldMetadata(alias="clientName"), pydantic.Field(alias="clientName")]
    uri: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FilePartSource = typing_extensions.Annotated[
    typing.Union[FilePartSource_File, FilePartSource_Symbol, FilePartSource_Resource],
    pydantic.Field(discriminator="type"),
]
