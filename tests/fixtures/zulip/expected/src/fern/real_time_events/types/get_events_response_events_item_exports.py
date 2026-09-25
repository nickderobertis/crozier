

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.realm_export import RealmExport
from .get_events_response_events_item_exports_type import GetEventsResponseEventsItemExportsType


class GetEventsResponseEventsItemExports(UniversalBaseModel):
    """
    Event sent to organization administrators when the
    status of a public or standard
    [data export](/help/export-your-organization)
    in the organization changes.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemExportsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    exports: typing.Optional[typing.List[RealmExport]] = pydantic.Field(default=None)
    """
    An array of dictionaries where each dictionary contains
    details about a data export of the organization.
    
    **Changes**: Prior to Zulip 10.0 (feature level 304), `export_type`
    parameter was not present as only public data export was supported via API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
