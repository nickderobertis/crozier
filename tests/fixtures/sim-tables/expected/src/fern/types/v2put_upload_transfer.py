

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2PutUploadTransfer(UniversalBaseModel):
    """
    Instructions for uploading bytes to one signed URL.
    """

    url: str = pydantic.Field()
    """
    Signed URL to which the file bytes are uploaded. Upload bytes with `PUT` and exactly the supplied headers; never construct or modify the signed URL. Treat any `2xx` as success. Sim-hosted URLs return an empty `204` and v2 JSON errors. Object-storage URLs may return `200` or `201` and provider-specific errors, often XML.
    """

    headers: typing.Dict[str, str] = pydantic.Field()
    """
    Headers that must be included with the upload request.
    """

    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="ISO 8601 expiration time for this signed URL. This is the URL's own expiry and is normally earlier than the upload session's expiresAt: the session stays open for later part, status, completion, and abort requests, but the bytes must be uploaded before this time. Once it passes, the storage provider rejects the upload and a new upload session must be created.",
        ),
    ]
    """
    ISO 8601 expiration time for this signed URL. This is the URL's own expiry and is normally earlier than the upload session's expiresAt: the session stays open for later part, status, completion, and abort requests, but the bytes must be uploaded before this time. Once it passes, the storage provider rejects the upload and a new upload session must be created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
