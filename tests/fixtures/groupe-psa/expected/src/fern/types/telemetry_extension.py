

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .maintenance_base import MaintenanceBase
from .position_base import PositionBase


class TelemetryExtension(UniversalBaseModel):
    """
    Additional data set for telemetry.
    """

    location: typing.Optional[PositionBase] = None
    maintenance: typing.Optional[MaintenanceBase] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
