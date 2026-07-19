

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hashedrekord_schema_signature_public_key import HashedrekordSchemaSignaturePublicKey


class HashedrekordSchemaSignature(UniversalBaseModel):
    """
    Information about the detached signature associated with the entry
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the content of the signature inline within the document
    """

    public_key: typing_extensions.Annotated[
        typing.Optional[HashedrekordSchemaSignaturePublicKey],
        FieldMetadata(alias="publicKey"),
        pydantic.Field(
            alias="publicKey",
            description="The public key that can verify the signature; this can also be an X509 code signing certificate that contains the raw public key information",
        ),
    ] = None
    """
    The public key that can verify the signature; this can also be an X509 code signing certificate that contains the raw public key information
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
