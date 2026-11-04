

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UploadFileResponse(UniversalBaseModel):
    s3uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="s3_uri"),
        pydantic.Field(alias="s3_uri", description="S3 URI where the file was uploaded"),
    ]
    """
    S3 URI where the file was uploaded
    """

    presigned_url: str = pydantic.Field()
    """
    Presigned URL to access the uploaded file
    """

    file_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier for this upload. Pass it to DELETE /v1/files/{file_id} to delete the file.
    """

    expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the file will be deleted, if a retention_days was supplied. Null means the file has no expiry of its own and follows the organization's data retention policy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
