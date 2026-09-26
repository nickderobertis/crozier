

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class VehicleItemLinks(UniversalBaseModel):
    self_: typing_extensions.Annotated[Link, FieldMetadata(alias="self"), pydantic.Field(alias="self")]
    fleet: typing.Optional[Link] = None
    last_position: typing_extensions.Annotated[
        typing.Optional[Link], FieldMetadata(alias="lastPosition"), pydantic.Field(alias="lastPosition")
    ] = None
    trips: typing.Optional[Link] = None
    maintenance: typing.Optional[Link] = None
    alerts: typing.Optional[Link] = None
    status: typing.Optional[Link] = None
    telemetry: typing.Optional[Link] = None
    monitors: typing.Optional[Link] = None
    remotes: typing.Optional[Link] = None
    callbacks: typing.Optional[Link] = None
    collisions: typing.Optional[Link] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
