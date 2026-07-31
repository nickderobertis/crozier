

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Folder(UniversalBaseModel):
    id: int
    notebook_id: typing_extensions.Annotated[int, FieldMetadata(alias="notebookId"), pydantic.Field(alias="notebookId")]
    name: str
    parent_folder_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="parentFolderId"), pydantic.Field(alias="parentFolderId")
    ] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    created_at: typing_extensions.Annotated[int, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[int, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    updated_by: typing_extensions.Annotated[str, FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
