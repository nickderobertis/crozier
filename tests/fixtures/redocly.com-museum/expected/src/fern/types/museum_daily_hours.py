

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date import Date


class MuseumDailyHours(UniversalBaseModel):
    """
    Daily operating hours for the museum.
    """

    date: Date = pydantic.Field()
    """
    Date the operating hours apply to.
    """

    time_open: typing_extensions.Annotated[str, FieldMetadata(alias="timeOpen")] = pydantic.Field()
    """
    Time the museum opens on a specific date. Uses 24 hour time format (`HH:mm`).
    """

    time_close: typing_extensions.Annotated[str, FieldMetadata(alias="timeClose")] = pydantic.Field()
    """
    Time the museum closes on a specific date. Uses 24 hour time format (`HH:mm`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
