

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .uuid_ import Uuid
from .viewer_kind import ViewerKind


class FileViewState(UniversalBaseModel):
    file_id: typing_extensions.Annotated[Uuid, FieldMetadata(alias="fileId"), pydantic.Field(alias="fileId")]
    kind: ViewerKind
    position: typing.Dict[str, typing.Any]
    preferences: typing.Dict[str, typing.Any]
    bookmarks: typing.List[typing.Dict[str, typing.Any]]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
