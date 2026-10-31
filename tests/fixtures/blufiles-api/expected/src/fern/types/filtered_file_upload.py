

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filtered_file_upload_status import FilteredFileUploadStatus


class FilteredFileUpload(UniversalBaseModel):
    id: str
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    current_bytes: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentBytes"), pydantic.Field(alias="currentBytes")
    ]
    total_bytes: typing_extensions.Annotated[str, FieldMetadata(alias="totalBytes"), pydantic.Field(alias="totalBytes")]
    status: FilteredFileUploadStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
