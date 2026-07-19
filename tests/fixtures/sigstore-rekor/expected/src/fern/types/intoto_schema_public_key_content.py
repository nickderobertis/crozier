

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .intoto_schema_public_key_content_hash import IntotoSchemaPublicKeyContentHash
from .intoto_schema_public_key_content_payload_hash import IntotoSchemaPublicKeyContentPayloadHash


class IntotoSchemaPublicKeyContent(UniversalBaseModel):
    envelope: typing.Optional[str] = pydantic.Field(default=None)
    """
    envelope
    """

    hash: typing.Optional[IntotoSchemaPublicKeyContentHash] = pydantic.Field(default=None)
    """
    Specifies the hash algorithm and value encompassing the entire signed envelope; this is computed by the rekor server, client-provided values are ignored
    """

    payload_hash: typing_extensions.Annotated[
        typing.Optional[IntotoSchemaPublicKeyContentPayloadHash],
        FieldMetadata(alias="payloadHash"),
        pydantic.Field(
            alias="payloadHash",
            description="Specifies the hash algorithm and value covering the payload within the DSSE envelope; this is computed by the rekor server, client-provided values are ignored",
        ),
    ] = None
    """
    Specifies the hash algorithm and value covering the payload within the DSSE envelope; this is computed by the rekor server, client-provided values are ignored
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
