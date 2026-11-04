

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .checksum import Checksum
from .upload_part_state import UploadPartState
from .uuid_ import Uuid


class UploadPart(UniversalBaseModel):
    upload_id: typing_extensions.Annotated[Uuid, FieldMetadata(alias="uploadId"), pydantic.Field(alias="uploadId")]
    part_no: typing_extensions.Annotated[int, FieldMetadata(alias="partNo"), pydantic.Field(alias="partNo")]
    state: UploadPartState
    plain_size: typing_extensions.Annotated[int, FieldMetadata(alias="plainSize"), pydantic.Field(alias="plainSize")]
    stored_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="storedSize"), pydantic.Field(alias="storedSize")
    ] = None
    checksum: typing.Optional[Checksum] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
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
