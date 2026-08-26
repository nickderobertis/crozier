

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .open_graph_metadata import OpenGraphMetadata


class FileInfo(UniversalBaseModel):
    children: typing.Optional[typing.List["FileInfo"]] = None
    id: str
    is_directory: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isDirectory"), pydantic.Field(alias="isDirectory")
    ]
    is_marimo_file: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isMarimoFile"), pydantic.Field(alias="isMarimoFile")
    ]
    last_modified: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    name: str
    opengraph: typing.Optional[OpenGraphMetadata] = None
    path: str
    size: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FileInfo)
