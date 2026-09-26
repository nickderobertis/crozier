

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v1bulk_hours_import_create_item_external_links_item import V1BulkHoursImportCreateItemExternalLinksItem
from .v1bulk_hours_import_create_item_timestamps_item import V1BulkHoursImportCreateItemTimestampsItem


class V1BulkHoursImportCreateItem(UniversalBaseModel):
    user_id: typing.Optional[int] = None
    project_id: int
    hours: typing.Optional[int] = None
    minutes: typing.Optional[int] = None
    seconds: typing.Optional[int] = None
    from_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[str] = None
    day: str
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
    timestamps: typing.Optional[typing.List[V1BulkHoursImportCreateItemTimestampsItem]] = None
    external_links: typing.Optional[typing.List[V1BulkHoursImportCreateItemExternalLinksItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
