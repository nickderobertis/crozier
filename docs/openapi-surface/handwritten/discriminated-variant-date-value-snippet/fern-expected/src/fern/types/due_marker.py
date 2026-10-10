

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DueMarker_Calendar(UniversalBaseModel):
    basis: typing.Literal["calendar"] = "calendar"
    value: dt.date

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DueMarker_Exact(UniversalBaseModel):
    basis: typing.Literal["exact"] = "exact"
    value: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DueMarker = typing_extensions.Annotated[
    typing.Union[DueMarker_Calendar, DueMarker_Exact], pydantic.Field(discriminator="basis")
]
