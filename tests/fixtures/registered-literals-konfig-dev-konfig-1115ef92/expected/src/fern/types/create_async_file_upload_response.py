

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateAsyncFileUploadResponse(UniversalBaseModel):
    """
    The pre-signed file upload URI and unique identifier of the request.
    """

    id: str = pydantic.Field()
    """
    The unique identifier for the request.
    """

    uri: str = pydantic.Field()
    """
    The pre-signed S3 link that should be used to upload the file.
    The maximum size accepted for this document is 50 MB.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
