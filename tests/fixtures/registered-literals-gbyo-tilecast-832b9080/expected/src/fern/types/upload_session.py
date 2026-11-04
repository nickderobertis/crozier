

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .upload_status import UploadStatus


class UploadSession(UniversalBaseModel):
    id: str
    filename: str
    mime_type: typing_extensions.Annotated[str, FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")]
    size_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="sizeBytes"), pydantic.Field(alias="sizeBytes")]
    offset: int
    status: UploadStatus
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    asset_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assetId"), pydantic.Field(alias="assetId")
    ] = None
    upload_endpoint: typing_extensions.Annotated[
        str, FieldMetadata(alias="uploadEndpoint"), pydantic.Field(alias="uploadEndpoint")
    ]
    maximum_size_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="maximumSizeBytes"), pydantic.Field(alias="maximumSizeBytes")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
