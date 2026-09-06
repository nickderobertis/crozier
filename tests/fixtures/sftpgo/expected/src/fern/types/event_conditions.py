

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .condition_options import ConditionOptions
from .event_conditions_fs_events_item import EventConditionsFsEventsItem
from .event_conditions_provider_events_item import EventConditionsProviderEventsItem
from .schedule import Schedule


class EventConditions(UniversalBaseModel):
    fs_events: typing.Optional[typing.List[EventConditionsFsEventsItem]] = None
    provider_events: typing.Optional[typing.List[EventConditionsProviderEventsItem]] = None
    schedules: typing.Optional[typing.List[Schedule]] = None
    idp_login_event: typing.Optional[int] = pydantic.Field(default=None)
    """
    IDP login events:
      - `0` any login event
      - `1` user login event
      - `2` admin login event
    """

    options: typing.Optional[ConditionOptions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
