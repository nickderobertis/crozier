

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checksum import Checksum


class CompletedUploadPart(UniversalBaseModel):
    """
    One uploaded part that the object store provider accepted.
    """

    checksum: Checksum = pydantic.Field()
    """
    The checksum that the part was signed and accepted with.
    """

    etag: str = pydantic.Field()
    """
    The entity tag that the provider returned for the accepted part.
    """

    part_number: int = pydantic.Field()
    """
    The part number, counting from 1.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
