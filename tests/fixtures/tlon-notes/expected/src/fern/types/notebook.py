

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Notebook(UniversalBaseModel):
    id: int
    title: str
    root_folder_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="rootFolderId"),
        pydantic.Field(
            alias="rootFolderId",
            description="Id of the notebook's root folder. Pass this as `parent` when creating a folder/note at the top level. Equal to `id + 1`.",
        ),
    ]
    """
    Id of the notebook's root folder. Pass this as `parent` when creating a folder/note at the top level. Equal to `id + 1`.
    """

    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    created_at: typing_extensions.Annotated[
        int, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt", description="Unix seconds")
    ]
    """
    Unix seconds
    """

    updated_at: typing_extensions.Annotated[int, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    updated_by: typing_extensions.Annotated[str, FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
