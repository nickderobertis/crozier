

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_event_rule import BaseEventRule
from .event_action import EventAction


class EventRule(BaseEventRule):
    actions: typing.Optional[typing.List[EventAction]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
