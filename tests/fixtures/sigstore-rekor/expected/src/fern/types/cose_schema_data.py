

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cose_schema_data_envelope_hash import CoseSchemaDataEnvelopeHash
from .cose_schema_data_payload_hash import CoseSchemaDataPayloadHash


class CoseSchemaData(UniversalBaseModel):
    """
    Information about the content associated with the entry
    """

    payload_hash: typing_extensions.Annotated[
        typing.Optional[CoseSchemaDataPayloadHash],
        FieldMetadata(alias="payloadHash"),
        pydantic.Field(alias="payloadHash", description="Specifies the hash algorithm and value for the content"),
    ] = None
    """
    Specifies the hash algorithm and value for the content
    """

    envelope_hash: typing_extensions.Annotated[
        typing.Optional[CoseSchemaDataEnvelopeHash],
        FieldMetadata(alias="envelopeHash"),
        pydantic.Field(
            alias="envelopeHash", description="Specifies the hash algorithm and value for the COSE envelope"
        ),
    ] = None
    """
    Specifies the hash algorithm and value for the COSE envelope
    """

    aad: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the additional authenticated data required to verify the signature
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
