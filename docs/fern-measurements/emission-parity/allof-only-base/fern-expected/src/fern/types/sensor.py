

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Sensor_Thermo(UniversalBaseModel):
    """
    Something that measures the air or the soil.
    """

    kind: typing.Literal["THERMO"] = "THERMO"
    celsius: typing.Optional[float] = None
    unit: typing.Optional[str] = None
    precision: typing.Optional[int] = None
    name: str
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Sensor_Rain(UniversalBaseModel):
    """
    Something that measures the air or the soil.
    """

    kind: typing.Literal["RAIN"] = "RAIN"
    millimetres: typing.Optional[float] = None
    bucket: typing.Optional[str] = None
    funnel_width: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="funnelWidth"), pydantic.Field(alias="funnelWidth")
    ] = None
    unit: typing.Optional[str] = None
    precision: typing.Optional[int] = None
    name: str
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Sensor_Wind(UniversalBaseModel):
    """
    Something that measures the air or the soil.
    """

    kind: typing.Literal["WIND"] = "WIND"
    heading: typing.Optional[float] = None
    degrees: typing.Optional[float] = None
    compass_point: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="compassPoint"), pydantic.Field(alias="compassPoint")
    ] = None
    unit: typing.Optional[str] = None
    precision: typing.Optional[int] = None
    name: str
    label: typing.Optional[str] = None
    calibrated_on: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="calibratedOn"), pydantic.Field(alias="calibratedOn")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Sensor_Humidity(UniversalBaseModel):
    """
    Something that measures the air or the soil.
    """

    kind: typing.Literal["HUMIDITY"] = "HUMIDITY"
    percent: typing.Optional[float] = None
    unit: typing.Optional[str] = None
    accuracy: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Sensor = typing_extensions.Annotated[
    typing.Union[Sensor_Thermo, Sensor_Rain, Sensor_Wind, Sensor_Humidity], pydantic.Field(discriminator="kind")
]
