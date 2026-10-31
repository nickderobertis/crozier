

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .filtered_file import FilteredFile


class FilteredFolder(UniversalBaseModel):
    id: str
    name: str
    owner_id: typing_extensions.Annotated[str, FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")]
    parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    files: typing.Optional[typing.List[FilteredFile]] = None
    folders: typing.Optional[typing.List["FilteredFolder"]] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    share_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="shareId"), pydantic.Field(alias="shareId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FilteredFolder)
