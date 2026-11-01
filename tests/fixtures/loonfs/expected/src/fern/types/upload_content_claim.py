

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checksum import Checksum


class UploadContentClaim(UniversalBaseModel):
    """
    The size and checksum of a complete direct upload payload.
    """

    checksum: Checksum = pydantic.Field()
    """
    The checksum of the whole payload, in the algorithm that this operation requires.
    """

    size_bytes: int = pydantic.Field()
    """
    The size of the complete payload in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
