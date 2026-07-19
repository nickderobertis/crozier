

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .jar_schema_signature_public_key import JarSchemaSignaturePublicKey


class JarSchemaSignature(UniversalBaseModel):
    """
    Information about the included signature in the JAR file
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the PKCS7 signature embedded within the JAR file 
    """

    public_key: typing_extensions.Annotated[
        typing.Optional[JarSchemaSignaturePublicKey],
        FieldMetadata(alias="publicKey"),
        pydantic.Field(
            alias="publicKey",
            description="The X509 certificate containing the public key JAR which verifies the signature of the JAR",
        ),
    ] = None
    """
    The X509 certificate containing the public key JAR which verifies the signature of the JAR
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
