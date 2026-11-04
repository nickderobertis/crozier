

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_part_file import FilePartFile


class PartOutput_Text(UniversalBaseModel):
    kind: typing.Literal["text"] = "text"
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PartOutput_File(UniversalBaseModel):
    kind: typing.Literal["file"] = "file"
    file: FilePartFile
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PartOutput_Data(UniversalBaseModel):
    kind: typing.Literal["data"] = "data"
    data: typing.Dict[str, typing.Any]
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PartOutput = typing_extensions.Annotated[
    typing.Union[PartOutput_Text, PartOutput_File, PartOutput_Data], pydantic.Field(discriminator="kind")
]
