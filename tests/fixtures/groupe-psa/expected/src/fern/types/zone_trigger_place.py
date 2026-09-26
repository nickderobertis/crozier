

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .zone_trigger_place_center import ZoneTriggerPlaceCenter


class ZoneTriggerPlace(UniversalBaseModel):
    """
    Circle zone is compound of a center point and a radius.
    """

    radius: int = pydantic.Field()
    """
    Circle radius (expressed in km)
    """

    center: ZoneTriggerPlaceCenter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
