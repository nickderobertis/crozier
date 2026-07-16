

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DisputeEvidenceFile(UniversalBaseModel):
    """
    A file to be uploaded as dispute evidence.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file name including the file extension. For example: "receipt.tiff".
    """

    filetype: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dispute evidence files must be application/pdf, image/heic, image/heif, image/jpeg, image/png, or image/tiff formats.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
