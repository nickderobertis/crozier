

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sync_keychain_vanilla_vanilla import SyncKeychainVanillaVanilla


class SyncKeychainVanilla(UniversalBaseModel):
    vanilla: typing_extensions.Annotated[
        SyncKeychainVanillaVanilla, FieldMetadata(alias="Vanilla"), pydantic.Field(alias="Vanilla")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
