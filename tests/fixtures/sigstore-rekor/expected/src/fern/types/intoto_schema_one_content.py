

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .intoto_schema_one_content_envelope import IntotoSchemaOneContentEnvelope
from .intoto_schema_one_content_hash import IntotoSchemaOneContentHash
from .intoto_schema_one_content_payload_hash import IntotoSchemaOneContentPayloadHash


class IntotoSchemaOneContent(UniversalBaseModel):
    envelope: IntotoSchemaOneContentEnvelope = pydantic.Field()
    """
    dsse envelope
    """

    hash: typing.Optional[IntotoSchemaOneContentHash] = pydantic.Field(default=None)
    """
    Specifies the hash algorithm and value encompassing the entire signed envelope
    """

    payload_hash: typing_extensions.Annotated[
        typing.Optional[IntotoSchemaOneContentPayloadHash],
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
