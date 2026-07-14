

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateMultipartUploadResponse(UniversalBaseModel):
    external_upload_identifier: str = pydantic.Field()
    """
    The identifier of the multipart upload in the external
    storage provider. This is the multipart upload_id in AWS S3.
    """

    key: str = pydantic.Field()
    """
    The path of the temporary file on the external storage
    service.
    """

    unique_identifier: str = pydantic.Field()
    """
    A unique string that identifies the external upload.
    This must be stored and then sent in the /complete-multipart
    and /batch-presign-multipart-parts endpoints.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
