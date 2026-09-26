

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v1forecast_estimated_duration import V1ForecastEstimatedDuration
from .v1forecast_logged_duration import V1ForecastLoggedDuration
from .v1forecast_planned_duration import V1ForecastPlannedDuration
from .v1forecast_project import V1ForecastProject
from .v1forecast_user import V1ForecastUser
from .v1forecast_users_item import V1ForecastUsersItem


class V1Forecast(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the task
    """

    note: str = pydantic.Field()
    """
    Task note (same as title, for backwards compatibility)
    """

    title: str = pydantic.Field()
    """
    Task title
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Detailed description of the task
    """

    from_: typing_extensions.Annotated[
        str, FieldMetadata(alias="from"), pydantic.Field(alias="from", description="Start date in ISO 8601 format")
    ]
    """
    Start date in ISO 8601 format
    """

    to: str = pydantic.Field()
    """
    End date in ISO 8601 format
    """

    user: typing.Optional[V1ForecastUser] = pydantic.Field(default=None)
    """
    Primary user assigned to the task
    """

    users: typing.List[V1ForecastUsersItem] = pydantic.Field()
    """
    All users assigned to the task
    """

    project: V1ForecastProject = pydantic.Field()
    """
    Project this task belongs to
    """

    estimated_minutes: int = pydantic.Field()
    """
    Estimated time in minutes
    """

    updated_at: str = pydantic.Field()
    """
    ISO 8601 timestamp of last modification
    """

    created_at: str = pydantic.Field()
    """
    ISO 8601 timestamp when task was created
    """

    label_ids: typing.List[int] = pydantic.Field()
    """
    Tags/categories applied to this task
    """

    estimated_duration: V1ForecastEstimatedDuration = pydantic.Field()
    """
    Estimated duration for the task
    """

    planned_duration: V1ForecastPlannedDuration = pydantic.Field()
    """
    Planned duration for the task
    """

    logged_duration: V1ForecastLoggedDuration = pydantic.Field()
    """
    Time already logged against this task
    """

    completed: bool = pydantic.Field()
    """
    Whether the task is marked as completed
    """

    completed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 8601 timestamp when task was completed
    """

    manage: bool = pydantic.Field()
    """
    True if current user can edit/delete this task
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Your system's identifier for integration mapping
    """

    parent_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the parent task (for subtasks)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
