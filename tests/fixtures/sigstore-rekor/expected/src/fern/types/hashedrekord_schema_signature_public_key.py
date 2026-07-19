

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HashedrekordSchemaSignaturePublicKey(UniversalBaseModel):
    """
    The public key that can verify the signature; this can also be an X509 code signing certificate that contains the raw public key information
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the content of the public key or code signing certificate inline within the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
