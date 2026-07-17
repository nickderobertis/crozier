

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_item_crafting_block_bonus_plug_definition import (
    DestinyDefinitionsDestinyItemCraftingBlockBonusPlugDefinition,
)


class DestinyDefinitionsDestinyItemCraftingBlockDefinition(UniversalBaseModel):
    """
    If an item can have an action performed on it (like "Dismantle"), it will be defined here if you care.
    """

    base_material_requirements: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="baseMaterialRequirements"),
        pydantic.Field(
            alias="baseMaterialRequirements",
            description="A reference to the base material requirements for crafting with this recipe.",
        ),
    ] = None
    """
    A reference to the base material requirements for crafting with this recipe.
    """

    bonus_plugs: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemCraftingBlockBonusPlugDefinition]],
        FieldMetadata(alias="bonusPlugs"),
        pydantic.Field(
            alias="bonusPlugs",
            description="A list of 'bonus' socket plugs that may be available if certain requirements are met.",
        ),
    ] = None
    """
    A list of 'bonus' socket plugs that may be available if certain requirements are met.
    """

    failed_requirement_strings: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="failedRequirementStrings"),
        pydantic.Field(alias="failedRequirementStrings"),
    ] = None
    output_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="outputItemHash"),
        pydantic.Field(
            alias="outputItemHash",
            description="A reference to the item definition that is created when crafting with this 'recipe' item.",
        ),
    ] = None
    """
    A reference to the item definition that is created when crafting with this 'recipe' item.
    """

    required_socket_type_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="requiredSocketTypeHashes"),
        pydantic.Field(
            alias="requiredSocketTypeHashes",
            description="A list of socket type hashes that describes which sockets are required for crafting with this recipe.",
        ),
    ] = None
    """
    A list of socket type hashes that describes which sockets are required for crafting with this recipe.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
