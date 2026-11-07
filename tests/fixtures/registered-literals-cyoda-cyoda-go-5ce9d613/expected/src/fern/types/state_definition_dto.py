

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .transition_definition_dto import TransitionDefinitionDto


class StateDefinitionDto(UniversalBaseModel):
    transitions: typing.Optional[typing.List[TransitionDefinitionDto]] = pydantic.Field(default=None)
    """
    List of possible transitions from this state
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(StateDefinitionDto)
