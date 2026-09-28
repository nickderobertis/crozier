

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2MultipartUploadTransfer(UniversalBaseModel):
    """
    Instructions for splitting bytes into a multipart upload.
    """

    part_size: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="partSize"),
        pydantic.Field(alias="partSize", description="Required size of each non-final part in bytes."),
    ]
    """
    Required size of each non-final part in bytes.
    """

    part_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="partCount"),
        pydantic.Field(alias="partCount", description="Total number of upload parts."),
    ]
    """
    Total number of upload parts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
