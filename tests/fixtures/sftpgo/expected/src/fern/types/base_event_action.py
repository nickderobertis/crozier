

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_event_action_options import BaseEventActionOptions
from .event_action_types import EventActionTypes


class BaseEventAction(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description
    """

    type: typing.Optional[EventActionTypes] = None
    options: typing.Optional[BaseEventActionOptions] = None
    rules: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of event rules names associated with this action
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
