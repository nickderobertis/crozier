

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dsse_schema_payload_hash_algorithm import DsseSchemaPayloadHashAlgorithm


class DsseSchemaPayloadHash(UniversalBaseModel):
    """
    Specifies the hash algorithm and value covering the payload within the DSSE envelope
    """

    algorithm: DsseSchemaPayloadHashAlgorithm = pydantic.Field()
    """
    The hashing function used to compute the hash value
    """

    value: str = pydantic.Field()
    """
    The value of the computed digest over the payload within the envelope
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
