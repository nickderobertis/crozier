

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_get_all_schedules_response_items_item_actor import ScheduleGetAllSchedulesResponseItemsItemActor
from .schedule_get_all_schedules_response_items_item_parameters_value import (
    ScheduleGetAllSchedulesResponseItemsItemParametersValue,
)
from .schedule_get_all_schedules_response_items_item_timetable import ScheduleGetAllSchedulesResponseItemsItemTimetable


class ScheduleGetAllSchedulesResponseItemsItem(UniversalBaseModel):
    """
    A schedule response
    """

    description: str = pydantic.Field()
    """
    Description of the schedule.
    """

    parameters: typing.Dict[str, ScheduleGetAllSchedulesResponseItemsItemParametersValue] = pydantic.Field()
    """
    Pipeline parameters represented as key-value pairs. Must contain branch or tag.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the schedule.
    """

    timetable: ScheduleGetAllSchedulesResponseItemsItemTimetable = pydantic.Field()
    """
    Timetable that specifies when a schedule triggers.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updated-at"),
        pydantic.Field(alias="updated-at", description="The date and time the pipeline was last updated."),
    ]
    """
    The date and time the pipeline was last updated.
    """

    name: str = pydantic.Field()
    """
    Name of the schedule.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="created-at"),
        pydantic.Field(alias="created-at", description="The date and time the pipeline was created."),
    ]
    """
    The date and time the pipeline was created.
    """

    project_slug: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="project-slug"),
        pydantic.Field(alias="project-slug", description="The project-slug for the schedule"),
    ]
    """
    The project-slug for the schedule
    """

    actor: ScheduleGetAllSchedulesResponseItemsItemActor = pydantic.Field()
    """
    The attribution actor who will run the scheduled pipeline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
