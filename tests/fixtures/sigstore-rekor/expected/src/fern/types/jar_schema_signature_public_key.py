

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JarSchemaSignaturePublicKey(UniversalBaseModel):
    """
    The X509 certificate containing the public key JAR which verifies the signature of the JAR
    """

    content: str = pydantic.Field()
    """
    Specifies the content of the X509 certificate containing the public key used to verify the signature
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
