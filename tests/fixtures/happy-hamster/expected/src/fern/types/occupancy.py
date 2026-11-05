

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Occupancy(UniversalBaseModel):
    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    Occupancy in percent.
    """

    count: int = pydantic.Field()
    """
    Number of datapoints used for the value calculation.
    """

    latest_report: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="latestReport"),
        pydantic.Field(
            alias="latestReport", description="Time of the latest report that was considered to calculate occupancy"
        ),
    ] = None
    """
    Time of the latest report that was considered to calculate occupancy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
