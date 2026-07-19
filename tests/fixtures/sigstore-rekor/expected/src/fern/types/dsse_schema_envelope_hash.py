

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dsse_schema_envelope_hash_algorithm import DsseSchemaEnvelopeHashAlgorithm


class DsseSchemaEnvelopeHash(UniversalBaseModel):
    """
    Specifies the hash algorithm and value encompassing the entire envelope sent to Rekor
    """

    algorithm: DsseSchemaEnvelopeHashAlgorithm = pydantic.Field()
    """
    The hashing function used to compute the hash value
    """

    value: str = pydantic.Field()
    """
    The value of the computed digest over the entire envelope
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
