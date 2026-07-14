

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GeneratePresignedPutResponse(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The path of the temporary file on the external storage
    service.
    """

    unique_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique string that identifies the external upload.
    This must be stored and then sent in the /complete-external-upload
    endpoint to complete the direct upload.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A presigned PUT URL which must be used to upload
    the file binary blob to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
