

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class FleetLinks(UniversalBaseModel):
    self_: typing_extensions.Annotated[Link, FieldMetadata(alias="self"), pydantic.Field(alias="self")]
    vehicles: typing.Optional[Link] = None
    status: typing.Optional[Link] = None
    maintenances: typing.Optional[Link] = None
    alerts: typing.Optional[Link] = None
    trips: typing.Optional[Link] = None
    collisions: typing.Optional[Link] = None
    monitors: typing.Optional[Link] = None
    callbacks: typing.Optional[Link] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
