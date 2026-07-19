

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .intoto_schema_one_content_hash_algorithm import IntotoSchemaOneContentHashAlgorithm


class IntotoSchemaOneContentHash(UniversalBaseModel):
    """
    Specifies the hash algorithm and value encompassing the entire signed envelope
    """

    algorithm: IntotoSchemaOneContentHashAlgorithm = pydantic.Field()
    """
    The hashing function used to compute the hash value
    """

    value: str = pydantic.Field()
    """
    The hash value for the archive
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
