

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_value_limit import ResourceValueLimit
from .resource_value_reservation import ResourceValueReservation


class ResourceValue(UniversalBaseModel):
    limit: ResourceValueLimit
    reservation: ResourceValueReservation

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
