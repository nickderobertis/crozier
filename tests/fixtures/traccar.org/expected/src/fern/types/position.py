

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .position_attributes import PositionAttributes
from .position_network import PositionNetwork


class Position(UniversalBaseModel):
    accuracy: typing.Optional[float] = None
    address: typing.Optional[str] = None
    altitude: typing.Optional[float] = None
    attributes: typing.Optional[PositionAttributes] = None
    course: typing.Optional[float] = None
    device_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="deviceId"), pydantic.Field(alias="deviceId")
    ] = None
    device_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deviceTime"),
        pydantic.Field(alias="deviceTime", description="in IS0 8601 format. eg. `1963-11-22T18:30:00Z`"),
    ] = None
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    fix_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="fixTime"),
        pydantic.Field(alias="fixTime", description="in IS0 8601 format. eg. `1963-11-22T18:30:00Z`"),
    ] = None
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    id: typing.Optional[int] = None
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    network: typing.Optional[PositionNetwork] = None
    outdated: typing.Optional[bool] = None
    protocol: typing.Optional[str] = None
    server_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="serverTime"),
        pydantic.Field(alias="serverTime", description="in IS0 8601 format. eg. `1963-11-22T18:30:00Z`"),
    ] = None
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    in knots
    """

    valid: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
