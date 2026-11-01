

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScheduleAvailabilityResponse(UniversalBaseModel):
    """
    Schedule availability response for given sku in a region.
    """

    available_dates: typing_extensions.Annotated[
        typing.Optional[typing.List[dt.datetime]],
        FieldMetadata(alias="availableDates"),
        pydantic.Field(alias="availableDates", description="List of dates available to schedule"),
    ] = None
    """
    List of dates available to schedule
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
