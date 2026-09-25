

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v1hour_cost import V1HourCost
from .v1hour_duration import V1HourDuration
from .v1hour_estimated_cost import V1HourEstimatedCost
from .v1hour_estimated_duration import V1HourEstimatedDuration
from .v1hour_estimated_internal_cost import V1HourEstimatedInternalCost
from .v1hour_external_links_item import V1HourExternalLinksItem
from .v1hour_internal_cost import V1HourInternalCost
from .v1hour_project import V1HourProject
from .v1hour_state import V1HourState
from .v1hour_timestamps_item import V1HourTimestampsItem
from .v1hour_user import V1HourUser


class V1Hour(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the time entry
    """

    uid: str = pydantic.Field()
    """
    Unique string identifier for the time entry
    """

    user: V1HourUser = pydantic.Field()
    """
    User who logged this time
    """

    project: V1HourProject = pydantic.Field()
    """
    Project this time was logged to
    """

    duration: V1HourDuration = pydantic.Field()
    """
    Actual time spent (use this for reported hours)
    """

    estimated_duration: V1HourEstimatedDuration = pydantic.Field()
    """
    Planned or estimated time
    """

    cost: V1HourCost = pydantic.Field()
    """
    Actual cost of this time entry
    """

    estimated_cost: V1HourEstimatedCost = pydantic.Field()
    """
    Estimated cost based on planned time
    """

    day: str = pydantic.Field()
    """
    Date this time was logged (YYYY-MM-DD format)
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description or notes about the work performed
    """

    sequence: int = pydantic.Field()
    """
    Order of this entry within the day
    """

    estimated: bool = pydantic.Field()
    """
    True for planned/scheduled time, false for actual logged time
    """

    timer_state: str = pydantic.Field()
    """
    Timer status: running, stopped, or paused
    """

    timer_started_on: int = pydantic.Field()
    """
    Unix timestamp when timer started (0 if not running)
    """

    timer_stopped_on: int = pydantic.Field()
    """
    Unix timestamp when timer stopped (0 if never stopped)
    """

    label_ids: typing.List[int] = pydantic.Field()
    """
    Tags/categories applied to this entry
    """

    user_ids: typing.List[int] = pydantic.Field()
    """
    Users associated with this entry (for team entries)
    """

    updated_at: int = pydantic.Field()
    """
    Unix timestamp of last modification
    """

    created_at: int = pydantic.Field()
    """
    Unix timestamp when entry was created
    """

    created_from: str = pydantic.Field()
    """
    Source that created this entry (web, mobile, api, etc.)
    """

    updated_from: str = pydantic.Field()
    """
    Source of last update (web, mobile, api, etc.)
    """

    billed: bool = pydantic.Field()
    """
    True if this time has been invoiced to the client
    """

    billable: bool = pydantic.Field()
    """
    True if this time can be billed to the client
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    End time in HH:MM format (24-hour)
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Start time in HH:MM format (24-hour)"),
    ] = None
    """
    Start time in HH:MM format (24-hour)
    """

    deleted: bool = pydantic.Field()
    """
    True if this entry has been deleted (soft delete)
    """

    hour_rate: float = pydantic.Field()
    """
    Billing rate per hour for this entry
    """

    hour_rate_in_cents: int = pydantic.Field()
    """
    Billing rate in cents (for precise calculations)
    """

    creator_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    User who created this entry
    """

    updater_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    User who last modified this entry
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Your system's identifier for integration mapping
    """

    entry_ids: typing.List[int] = pydantic.Field()
    """
    Memory timeline entries that make up this logged time
    """

    suggestion_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    AI suggestion that generated this entry
    """

    draft: bool = pydantic.Field()
    """
    True if this is a draft (not yet submitted)
    """

    manage: bool = pydantic.Field()
    """
    True if current user can edit/delete this entry
    """

    forecast_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Task that this entry fulfills
    """

    billed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 8601 timestamp when this was invoiced
    """

    external_link_ids: typing.List[int] = pydantic.Field()
    """
    Links to related resources (tickets, docs, etc.)
    """

    internal_cost: typing.Optional[V1HourInternalCost] = pydantic.Field(default=None)
    """
    Your internal cost for this work (for profit tracking)
    """

    estimated_internal_cost: typing.Optional[V1HourEstimatedInternalCost] = pydantic.Field(default=None)
    """
    Estimated internal cost
    """

    internal_cost_rate: int = pydantic.Field()
    """
    Internal cost rate in cents per hour
    """

    profit: int = pydantic.Field()
    """
    Profit margin in cents (billable cost - internal cost)
    """

    profitability: int = pydantic.Field()
    """
    Profit percentage ((profit / cost) * 100)
    """

    locked_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Why this entry is locked (e.g., "Approved timesheet")
    """

    locked: bool = pydantic.Field()
    """
    True if entry is locked and cannot be edited
    """

    invoice_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Invoice this entry appears on (if billed)
    """

    timestamps: typing.List[V1HourTimestampsItem] = pydantic.Field()
    """
    Individual time segments that make up this entry
    """

    state: typing.Optional[V1HourState] = pydantic.Field(default=None)
    """
    Workflow state (for approval processes)
    """

    external_links: typing.List[V1HourExternalLinksItem] = pydantic.Field()
    """
    Attached links to tickets, PRs, documents, etc.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
