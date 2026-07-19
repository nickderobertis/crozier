

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .intoto_schema_public_key_content import IntotoSchemaPublicKeyContent


class IntotoSchemaPublicKey(UniversalBaseModel):
    """
    Schema for intoto object
    """

    content: IntotoSchemaPublicKeyContent
    public_key: typing_extensions.Annotated[
        str,
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
