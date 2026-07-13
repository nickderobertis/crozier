

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_definitions_destiny_item_investment_stat_definition import (
    DestinyDefinitionsDestinyItemInvestmentStatDefinition,
)


class DestinyDefinitionsDestinyObjectiveStatEntryDefinition(UniversalBaseModel):
    """
    Defines the conditions under which stat modifications will be applied to a Character while participating in an objective.
    """

    stat: typing.Optional[DestinyDefinitionsDestinyItemInvestmentStatDefinition] = pydantic.Field(default=None)
    """
    The stat being modified, and the value used.
    """

    style: typing.Optional[int] = pydantic.Field(default=None)
    """
    Whether it will be applied as long as the objective is active, when it's completed, or until it's completed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
