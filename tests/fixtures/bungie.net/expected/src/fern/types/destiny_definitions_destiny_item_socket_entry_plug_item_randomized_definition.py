

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_plug_item_crafting_requirements import (
    DestinyDefinitionsDestinyPlugItemCraftingRequirements,
)


class DestinyDefinitionsDestinyItemSocketEntryPlugItemRandomizedDefinition(UniversalBaseModel):
    crafting_requirements: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyPlugItemCraftingRequirements],
        FieldMetadata(alias="craftingRequirements"),
    ] = None
    currently_can_roll: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="currentlyCanRoll")] = (
        pydantic.Field(default=None)
    )
    """
    Indicates if the plug can be rolled on the current version of the item. For example, older versions of weapons may have plug rolls that are no longer possible on the current versions.
    """

    plug_item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="plugItemHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
