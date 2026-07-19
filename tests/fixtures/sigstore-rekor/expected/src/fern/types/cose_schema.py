

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cose_schema_data import CoseSchemaData


class CoseSchema(UniversalBaseModel):
    """
    Schema for cose object
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The COSE Sign1 Message
    """

    public_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="The public key that can verify the signature"),
    ]
    """
    The public key that can verify the signature
    """

    data: typing.Optional[CoseSchemaData] = pydantic.Field(default=None)
    """
    Information about the content associated with the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
