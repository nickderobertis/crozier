

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_definitions_destiny_activity_loadout_requirement import (
    DestinyDefinitionsDestinyActivityLoadoutRequirement,
)


class DestinyDefinitionsDestinyActivityLoadoutRequirementSet(UniversalBaseModel):
    requirements: typing.Optional[typing.List[DestinyDefinitionsDestinyActivityLoadoutRequirement]] = pydantic.Field(
        default=None
    )
    """
    The set of requirements that will be applied on the activity if this requirement set is active.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
