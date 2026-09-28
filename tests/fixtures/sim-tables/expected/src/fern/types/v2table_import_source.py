

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2TableImportSource_Upload(UniversalBaseModel):
    """
    CSV source for the import.
    """

    type: typing.Literal["upload"] = "upload"
    name: str
    content_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ]
    size: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class V2TableImportSource_WorkspaceFile(UniversalBaseModel):
    """
    CSV source for the import.
    """

    type: typing.Literal["workspace_file"] = "workspace_file"
    file_id: typing_extensions.Annotated[str, FieldMetadata(alias="fileId"), pydantic.Field(alias="fileId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


V2TableImportSource = typing_extensions.Annotated[
    typing.Union[V2TableImportSource_Upload, V2TableImportSource_WorkspaceFile], pydantic.Field(discriminator="type")
]
