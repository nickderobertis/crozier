

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BenchlingAppManifestSecurity(UniversalBaseModel):
    public_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publicKey"),
        pydantic.Field(
            alias="publicKey",
            description='Public key used to encrypt secure_text values. The value is constrained:\n  * value must be a public key PEM certificate\n  * key type (kty) must be RSA\n  * algorithm must be RSAES_OAEP_SHA_256\n  * key size must be 2048 bits, with exponent=65537\n  * key usage (use) must not be "signing". It can be either unspecified, or "encrypt/decrypt"',
        ),
    ] = None
    """
    Public key used to encrypt secure_text values. The value is constrained:
      * value must be a public key PEM certificate
      * key type (kty) must be RSA
      * algorithm must be RSAES_OAEP_SHA_256
      * key size must be 2048 bits, with exponent=65537
      * key usage (use) must not be "signing". It can be either unspecified, or "encrypt/decrypt"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
