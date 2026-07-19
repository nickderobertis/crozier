

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hashedrekord_schema_data_hash_algorithm import HashedrekordSchemaDataHashAlgorithm


class HashedrekordSchemaDataHash(UniversalBaseModel):
    """
    Specifies the hash algorithm and value for the content
    """

    algorithm: HashedrekordSchemaDataHashAlgorithm = pydantic.Field()
    """
    The hashing function used to compute the hash value
    """

    value: str = pydantic.Field()
    """
    The hash value for the content, as represented by a lower case hexadecimal string
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
