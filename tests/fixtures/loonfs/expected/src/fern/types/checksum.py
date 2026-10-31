

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checksum_algorithm import ChecksumAlgorithm


class Checksum(UniversalBaseModel):
    """
    A checksum algorithm and the checksum's canonical lowercase hexadecimal value.
    """

    algorithm: ChecksumAlgorithm = pydantic.Field()
    """
    The algorithm that produced `value`.
    """

    value: str = pydantic.Field()
    """
    The checksum in canonical lowercase hexadecimal, without a prefix.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
