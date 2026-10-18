

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dsse_schema_envelope_hash import DsseSchemaEnvelopeHash
from .dsse_schema_payload_hash import DsseSchemaPayloadHash
from .dsse_schema_proposed_content import DsseSchemaProposedContent
from .dsse_schema_signatures_item import DsseSchemaSignaturesItem


class DsseSchema(UniversalBaseModel):
    """
    Schema for DSSE envelopes
    """

    proposed_content: typing_extensions.Annotated[
        typing.Optional[DsseSchemaProposedContent],
        FieldMetadata(alias="proposedContent"),
        pydantic.Field(alias="proposedContent"),
    ] = None
    signatures: typing.Optional[typing.List[DsseSchemaSignaturesItem]] = pydantic.Field(default=None)
    """
    extracted collection of all signatures of the envelope's payload; elements will be sorted by lexicographical order of the base64 encoded signature strings
    """

    envelope_hash: typing_extensions.Annotated[
        typing.Optional[DsseSchemaEnvelopeHash],
        FieldMetadata(alias="envelopeHash"),
        pydantic.Field(
            alias="envelopeHash",
            description="Specifies the hash algorithm and value encompassing the entire envelope sent to Rekor",
        ),
    ] = None
    """
    Specifies the hash algorithm and value encompassing the entire envelope sent to Rekor
    """

    payload_hash: typing_extensions.Annotated[
        typing.Optional[DsseSchemaPayloadHash],
        FieldMetadata(alias="payloadHash"),
        pydantic.Field(
            alias="payloadHash",
            description="Specifies the hash algorithm and value covering the payload within the DSSE envelope",
        ),
    ] = None
    """
    Specifies the hash algorithm and value covering the payload within the DSSE envelope
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
