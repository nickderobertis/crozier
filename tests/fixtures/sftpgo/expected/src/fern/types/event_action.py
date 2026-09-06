

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_event_action import BaseEventAction
from .event_action_options import EventActionOptions


class EventAction(BaseEventAction):
    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    execution order
    """

    relation_options: typing.Optional[EventActionOptions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
