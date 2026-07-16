

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .maintenance_attributes import MaintenanceAttributes


class Maintenance(UniversalBaseModel):
    attributes: typing.Optional[MaintenanceAttributes] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    period: typing.Optional[float] = None
    start: typing.Optional[float] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
