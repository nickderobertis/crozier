

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonEventRead(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    The type of the event in the CRM.
    """

    subject: str = pydantic.Field()
    """
    The Subject of the event/meeting in the CRM.
    """

    start_date_time: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="startDateTime"),
        pydantic.Field(alias="startDateTime", description="Event start date time."),
    ]
    """
    Event start date time.
    """

    end_date_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="endDateTime"), pydantic.Field(alias="endDateTime", description="Event end date time.")
    ]
    """
    Event end date time.
    """

    is_all_day_event: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isAllDayEvent"),
        pydantic.Field(alias="isAllDayEvent", description="Is `true` if the event is an all day event."),
    ]
    """
    Is `true` if the event is an all day event.
    """

    description: str = pydantic.Field()
    """
    Description of the event/meeting.
    """

    location: str = pydantic.Field()
    """
    The location of the event/meeting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
