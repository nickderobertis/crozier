

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_collectibles_destiny_collectible_definition import (
    DestinyDefinitionsCollectiblesDestinyCollectibleDefinition,
)
from .destiny_definitions_destiny_inventory_item_definition import DestinyDefinitionsDestinyInventoryItemDefinition


class TokensCollectibleDefinitions(UniversalBaseModel):
    collectible_definition: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCollectiblesDestinyCollectibleDefinition],
        FieldMetadata(alias="CollectibleDefinition"),
    ] = None
    destiny_inventory_item_definition: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyInventoryItemDefinition],
        FieldMetadata(alias="DestinyInventoryItemDefinition"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
