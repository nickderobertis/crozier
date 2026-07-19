

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IntotoSchemaOneContentEnvelopeSignaturesItem(UniversalBaseModel):
    """
    a signature of the envelope's payload along with the public key for the signature
    """

    keyid: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional id of the key used to create the signature
    """

    sig: str = pydantic.Field()
    """
    signature of the payload
    """

    public_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="public key that corresponds to this signature"),
    ]
    """
    public key that corresponds to this signature
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
