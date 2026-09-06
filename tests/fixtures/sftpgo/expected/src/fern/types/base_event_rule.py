

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_conditions import EventConditions
from .event_trigger_types import EventTriggerTypes


class BaseEventRule(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique name
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    status:
      * `0` disabled
      * `1` enabled
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    creation time as unix timestamp in milliseconds
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    last update time as unix timestamp in millisecond
    """

    trigger: typing.Optional[EventTriggerTypes] = None
    conditions: typing.Optional[EventConditions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
