

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dek_algorithm import DekAlgorithm


class Dek(UniversalBaseModel):
    kek_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kekName"), pydantic.Field(alias="kekName")
    ] = None
    subject: typing.Optional[str] = None
    version: typing.Optional[int] = None
    algorithm: typing.Optional[DekAlgorithm] = None
    encrypted_key_material: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="encryptedKeyMaterial"), pydantic.Field(alias="encryptedKeyMaterial")
    ] = None
    key_material: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="keyMaterial"), pydantic.Field(alias="keyMaterial")
    ] = None
    ts: typing.Optional[int] = None
    deleted: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
