

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RekorSchemaSignaturePublicKey(UniversalBaseModel):
    """
    The public key that can verify the signature
    """

    content: str = pydantic.Field()
    """
    Specifies the content of the public key inline within the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
