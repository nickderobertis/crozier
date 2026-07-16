

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .location_status_label import LocationStatusLabel
from .location_status_value import LocationStatusValue


class LocationStatus(UniversalBaseModel):
    label: LocationStatusLabel
    value: LocationStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
