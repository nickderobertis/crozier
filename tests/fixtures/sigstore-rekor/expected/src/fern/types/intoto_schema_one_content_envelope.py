

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .intoto_schema_one_content_envelope_signatures_item import IntotoSchemaOneContentEnvelopeSignaturesItem


class IntotoSchemaOneContentEnvelope(UniversalBaseModel):
    """
    dsse envelope
    """

    payload: typing.Optional[str] = pydantic.Field(default=None)
    """
    payload of the envelope
    """

    payload_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="payloadType"),
        pydantic.Field(alias="payloadType", description="type describing the payload"),
    ]
    """
    type describing the payload
    """

    signatures: typing.List[IntotoSchemaOneContentEnvelopeSignaturesItem] = pydantic.Field()
    """
    collection of all signatures of the envelope's payload
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
