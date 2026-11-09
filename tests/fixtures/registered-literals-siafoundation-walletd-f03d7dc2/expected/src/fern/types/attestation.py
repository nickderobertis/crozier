

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .public_key import PublicKey
from .signature import Signature


class Attestation(UniversalBaseModel):
    public_key: typing_extensions.Annotated[
        PublicKey, FieldMetadata(alias="publicKey"), pydantic.Field(alias="publicKey")
    ]
    key: str
    value: str
    signature: Signature

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
