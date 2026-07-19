

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .intoto_schema_public_key_content_payload_hash_algorithm import IntotoSchemaPublicKeyContentPayloadHashAlgorithm


class IntotoSchemaPublicKeyContentPayloadHash(UniversalBaseModel):
    """
    Specifies the hash algorithm and value covering the payload within the DSSE envelope; this is computed by the rekor server, client-provided values are ignored
    """

    algorithm: IntotoSchemaPublicKeyContentPayloadHashAlgorithm = pydantic.Field()
    """
    The hashing function used to compute the hash value
    """

    value: str = pydantic.Field()
    """
    The hash value for the envelope's payload
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
