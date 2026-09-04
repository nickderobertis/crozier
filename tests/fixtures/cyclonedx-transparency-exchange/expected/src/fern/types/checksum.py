

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .checksum_type import ChecksumType


class Checksum(UniversalBaseModel):
    alg_type: typing_extensions.Annotated[
        ChecksumType, FieldMetadata(alias="algType"), pydantic.Field(alias="algType", description="Checksum algorithm")
    ]
    """
    Checksum algorithm
    """

    alg_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="algValue"), pydantic.Field(alias="algValue", description="Checksum value")
    ]
    """
    Checksum value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
