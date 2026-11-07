

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FileUploadTarget(UniversalBaseModel):
    """
    Where to send a file's bytes after staging it in presigned mode. There is no per-file completion call — finalise verifies the upload.
    """

    upload_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="uploadUrl"),
        pydantic.Field(
            alias="uploadUrl",
            description="The URL to upload the file's bytes to, typically a presigned object-store URL.",
        ),
    ]
    """
    The URL to upload the file's bytes to, typically a presigned object-store URL.
    """

    method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HTTP method to use for the upload.
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Headers the client MUST include in the upload request.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="When the upload target stops accepting bytes. Re-stage the file to obtain a fresh target.",
        ),
    ] = None
    """
    When the upload target stops accepting bytes. Re-stage the file to obtain a fresh target.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
