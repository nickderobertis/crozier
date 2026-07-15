

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .expires_at import ExpiresAt
from .id import Id


class UploadSession(UniversalBaseModel):
    expires_at: typing.Optional[ExpiresAt] = None
    id: typing.Optional[Id] = None
    parallel_upload_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if parts of the file can uploaded in parallel.
    """

    part_size: typing.Optional[float] = pydantic.Field(default=None)
    """
    Size in bytes of each part of the file that you will upload. Uploaded parts need to be this size for the upload to be successful.
    """

    success: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the upload session was completed successfully.
    """

    uploaded_byte_range: typing.Optional[str] = pydantic.Field(default=None)
    """
    The range of bytes that was successfully uploaded.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
