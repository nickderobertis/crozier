

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .transition_definition_dto_criterion import TransitionDefinitionDtoCriterion
from .transition_definition_dto_processors_item import TransitionDefinitionDtoProcessorsItem


class TransitionDefinitionDto(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the transition
    """

    next: str = pydantic.Field()
    """
    Target state code for this transition
    """

    manual: bool = pydantic.Field()
    """
    Whether this transition requires manual triggering
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Flag indicating if the transition is disabled
    """

    processors: typing.Optional[typing.List[TransitionDefinitionDtoProcessorsItem]] = pydantic.Field(default=None)
    """
    List of processors to execute for this transition
    """

    criterion: typing.Optional[TransitionDefinitionDtoCriterion] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(TransitionDefinitionDto)
