

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Note(UniversalBaseModel):
    id: int
    notebook_id: typing_extensions.Annotated[int, FieldMetadata(alias="notebookId"), pydantic.Field(alias="notebookId")]
    folder_id: typing_extensions.Annotated[int, FieldMetadata(alias="folderId"), pydantic.Field(alias="folderId")]
    title: str
    slug: typing.Optional[str] = None
    body_md: typing_extensions.Annotated[str, FieldMetadata(alias="bodyMd"), pydantic.Field(alias="bodyMd")]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    created_at: typing_extensions.Annotated[int, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_by: typing_extensions.Annotated[str, FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")]
    updated_at: typing_extensions.Annotated[int, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    revision: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
