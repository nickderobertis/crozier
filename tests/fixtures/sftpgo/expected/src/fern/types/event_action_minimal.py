

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_action_options import EventActionOptions


class EventActionMinimal(UniversalBaseModel):
    name: typing.Optional[str] = None
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
