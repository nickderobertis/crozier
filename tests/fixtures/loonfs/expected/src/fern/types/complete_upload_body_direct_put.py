

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upload_content_claim import UploadContentClaim


class CompleteUploadBodyDirectPut(UniversalBaseModel):
    """
    The completion of a direct PUT upload.
    """

    content: UploadContentClaim = pydantic.Field()
    """
    The expected length and checksum of the stored object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
