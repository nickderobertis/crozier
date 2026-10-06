

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class BaseCalendar(UniversalBaseModel):
    name: typing.Optional[str] = None
    eras: typing.Optional[typing.List["Era"]] = None
    calendar_date: typing_extensions.Annotated[
        typing.Optional["CalendarDate"], FieldMetadata(alias="calendarDate"), pydantic.Field(alias="calendarDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .calendar_date import CalendarDate
from .era import Era

update_forward_refs(BaseCalendar, CalendarDate=CalendarDate, Era=Era)
