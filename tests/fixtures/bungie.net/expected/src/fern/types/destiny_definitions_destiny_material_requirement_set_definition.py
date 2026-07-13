

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_definitions_destiny_material_requirement import DestinyDefinitionsDestinyMaterialRequirement


class DestinyDefinitionsDestinyMaterialRequirementSetDefinition(UniversalBaseModel):
    """
    Represent a set of material requirements: Items that either need to be owned or need to be consumed in order to perform an action.
    A variety of other entities refer to these as gatekeepers and payments for actions that can be performed in game.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    materials: typing.Optional[typing.List[DestinyDefinitionsDestinyMaterialRequirement]] = pydantic.Field(default=None)
    """
    The list of all materials that are required.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
