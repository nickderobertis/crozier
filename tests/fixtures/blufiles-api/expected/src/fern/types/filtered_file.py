

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilteredFile(UniversalBaseModel):
    id: str
    name: str
    mime: str
    size: str
    owner_id: typing_extensions.Annotated[str, FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")]
    folder_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="folderId"), pydantic.Field(alias="folderId")
    ] = None
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
