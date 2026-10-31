

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checksum import Checksum


class UploadPartChecksumClaim(UniversalBaseModel):
    """
    One upload part number and its checksum.
    """

    checksum: Checksum = pydantic.Field()
    """
    The checksum of this part's bytes.
    """

    part_number: int = pydantic.Field()
    """
    The part number, counting from 1. The number can't exceed the provider's limit of 10,000
    parts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
