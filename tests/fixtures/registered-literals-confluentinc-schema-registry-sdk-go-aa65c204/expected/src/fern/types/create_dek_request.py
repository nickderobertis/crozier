

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_dek_request_algorithm import CreateDekRequestAlgorithm


class CreateDekRequest(UniversalBaseModel):
    subject: typing.Optional[str] = None
    version: typing.Optional[int] = None
    algorithm: typing.Optional[CreateDekRequestAlgorithm] = None
    encrypted_key_material: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="encryptedKeyMaterial"), pydantic.Field(alias="encryptedKeyMaterial")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
