

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .name_conflict_policy import NameConflictPolicy
from .uuid_ import Uuid


class FolderCreateRequest(UniversalBaseModel):
    parent_id: typing_extensions.Annotated[
        typing.Optional[Uuid], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    name: str
    conflict_policy: typing_extensions.Annotated[
        typing.Optional[NameConflictPolicy],
        FieldMetadata(alias="conflictPolicy"),
        pydantic.Field(alias="conflictPolicy"),
    ] = None
    mod_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modTime"), pydantic.Field(alias="modTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
