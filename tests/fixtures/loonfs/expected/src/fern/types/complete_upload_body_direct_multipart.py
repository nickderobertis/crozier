

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completed_upload_part import CompletedUploadPart
from .upload_content_claim import UploadContentClaim


class CompleteUploadBodyDirectMultipart(UniversalBaseModel):
    """
    The completion of a direct multipart upload.
    """

    content: UploadContentClaim = pydantic.Field()
    """
    The expected length and checksum of the assembled object.
    """

    parts: typing.List[CompletedUploadPart] = pydantic.Field()
    """
    The uploaded parts, in ascending part order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
