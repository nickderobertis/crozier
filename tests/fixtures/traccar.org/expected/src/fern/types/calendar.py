

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .calendar_attributes import CalendarAttributes


class Calendar(UniversalBaseModel):
    attributes: typing.Optional[CalendarAttributes] = None
    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    base64 encoded in iCalendar format
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
