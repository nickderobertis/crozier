

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .zone_trigger_place import ZoneTriggerPlace
from .zone_trigger_transition import ZoneTriggerTransition


class ZoneTrigger(UniversalBaseModel):
    """
    Zone Alert parameter object
    """

    transition: ZoneTriggerTransition = pydantic.Field()
    """
    Zone monitoring type ('In' for monitoring entering zone and 'Out' for monitoring leaving zone),
    """

    place: ZoneTriggerPlace = pydantic.Field()
    """
    Circle zone is compound of a center point and a radius.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
