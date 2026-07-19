

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rekor_schema_signature_format import RekorSchemaSignatureFormat
from .rekor_schema_signature_public_key import RekorSchemaSignaturePublicKey


class RekorSchemaSignature(UniversalBaseModel):
    """
    Information about the detached signature associated with the entry
    """

    format: RekorSchemaSignatureFormat = pydantic.Field()
    """
    Specifies the format of the signature
    """

    content: str = pydantic.Field()
    """
    Specifies the content of the signature inline within the document
    """

    public_key: typing_extensions.Annotated[
        RekorSchemaSignaturePublicKey,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="The public key that can verify the signature"),
    ]
    """
    The public key that can verify the signature
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
