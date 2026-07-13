

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_plug_item_crafting_unlock_requirement import (
    DestinyDefinitionsDestinyPlugItemCraftingUnlockRequirement,
)


class DestinyDefinitionsDestinyPlugItemCraftingRequirements(UniversalBaseModel):
    material_requirement_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="materialRequirementHashes")
    ] = None
    required_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="requiredLevel")] = (
        pydantic.Field(default=None)
    )
    """
    If the plug has a known level requirement, it'll be available here.
    """

    unlock_requirements: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyPlugItemCraftingUnlockRequirement]],
        FieldMetadata(alias="unlockRequirements"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
