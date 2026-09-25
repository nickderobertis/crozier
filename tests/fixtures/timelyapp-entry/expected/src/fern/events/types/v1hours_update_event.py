

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .v1hours_update_event_external_links_item import V1HoursUpdateEventExternalLinksItem
from .v1hours_update_event_timestamps_item import V1HoursUpdateEventTimestampsItem


class V1HoursUpdateEvent(UniversalBaseModel):
    user_id: typing.Optional[int] = None
    project_id: typing.Optional[int] = None
    hours: typing.Optional[int] = None
    minutes: typing.Optional[int] = None
    seconds: typing.Optional[int] = None
    from_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[str] = None
    day: typing.Optional[str] = None
    note: typing.Optional[str] = None
    sequence: typing.Optional[int] = None
    estimated_hours: typing.Optional[int] = None
    estimated_minutes: typing.Optional[int] = None
    billed: typing.Optional[bool] = None
    locked: typing.Optional[bool] = None
    billable: typing.Optional[bool] = None
    hour_rate: typing.Optional[float] = None
    internal_hour_rate: typing.Optional[float] = None
    timer_state: typing.Optional[int] = None
    suggestion_id: typing.Optional[int] = None
    external_id: typing.Optional[str] = None
    forecast_id: typing.Optional[int] = None
    forecast_completed_at: typing.Optional[str] = None
    state_id: typing.Optional[int] = None
    label_ids: typing.Optional[typing.List[int]] = None
    user_ids: typing.Optional[typing.List[int]] = None
    entry_ids: typing.Optional[typing.List[int]] = None
    timestamps: typing.Optional[typing.List[V1HoursUpdateEventTimestampsItem]] = None
    external_links: typing.Optional[typing.List[V1HoursUpdateEventExternalLinksItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
