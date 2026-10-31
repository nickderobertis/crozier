

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filtered_file import FilteredFile


class FilteredCollection(UniversalBaseModel):
    id: str
    name: str
    owner_id: typing_extensions.Annotated[str, FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    files: typing.Optional[typing.List[FilteredFile]] = None
    count: typing.Optional[float] = None
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
