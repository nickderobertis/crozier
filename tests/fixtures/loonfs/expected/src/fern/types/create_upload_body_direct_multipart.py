

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateUploadBodyDirectMultipart(UniversalBaseModel):
    """
    A transport in which the client writes the object in parts through presigned part uploads.
    """

    part_size_bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The byte length of every part except the last. Omit it to use the server default.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
