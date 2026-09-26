

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_content_patch_hunks_item import FileContentPatchHunksItem


class FileContentPatch(UniversalBaseModel):
    old_file_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="oldFileName"), pydantic.Field(alias="oldFileName")
    ]
    new_file_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="newFileName"), pydantic.Field(alias="newFileName")
    ]
    old_header: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldHeader"), pydantic.Field(alias="oldHeader")
    ] = None
    new_header: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newHeader"), pydantic.Field(alias="newHeader")
    ] = None
    hunks: typing.List[FileContentPatchHunksItem]
    index: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
