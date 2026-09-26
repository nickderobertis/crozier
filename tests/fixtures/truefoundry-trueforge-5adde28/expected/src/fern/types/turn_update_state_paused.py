

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_required import ActionRequired


class TurnUpdateStatePaused(UniversalBaseModel):
    action_required_on_events: typing.List[ActionRequired] = pydantic.Field()
    """
    Events that still need a user or client action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
