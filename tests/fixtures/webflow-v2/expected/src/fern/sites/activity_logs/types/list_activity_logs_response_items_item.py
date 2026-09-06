

import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_activity_logs_response_items_item_actor_type import ListActivityLogsResponseItemsItemActorType
from .list_activity_logs_response_items_item_event import ListActivityLogsResponseItemsItemEvent
from .list_activity_logs_response_items_item_resource_operation import (
    ListActivityLogsResponseItemsItemResourceOperation,
)
from .list_activity_logs_response_items_item_source import ListActivityLogsResponseItemsItemSource
from .list_activity_logs_response_items_item_user import ListActivityLogsResponseItemsItemUser


class ListActivityLogsResponseItemsItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdOn"), pydantic.Field(alias="createdOn")
    ] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    event: typing.Optional[ListActivityLogsResponseItemsItemEvent] = None
    resource_operation: typing_extensions.Annotated[
        typing.Optional[ListActivityLogsResponseItemsItemResourceOperation],
        FieldMetadata(alias="resourceOperation"),
        pydantic.Field(alias="resourceOperation"),
    ] = None
    user: typing.Optional[ListActivityLogsResponseItemsItemUser] = None
    resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")
    ] = None
    resource_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceName"), pydantic.Field(alias="resourceName")
    ] = None
    new_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newValue"), pydantic.Field(alias="newValue")
    ] = None
    previous_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="previousValue"), pydantic.Field(alias="previousValue")
    ] = None
    payload: typing.Optional[typing.Dict[str, typing.Any]] = None
    source: typing.Optional[ListActivityLogsResponseItemsItemSource] = pydantic.Field(default=None)
    """
    The system that originated the event. `WEBFLOW_AI` for Webflow AI features, `WEBFLOW_MCP` for an external MCP server or Bridge App, `DESIGNER` for human writes from the Designer, and `SYSTEM` for automated Webflow processes such as backups or migrations. `null` for legacy events recorded before attribution was available.
    """

    actor_type: typing_extensions.Annotated[
        typing.Optional[ListActivityLogsResponseItemsItemActorType],
        FieldMetadata(alias="actorType"),
        pydantic.Field(
            alias="actorType",
            description="The type of actor responsible for the event. `user` for a human who directly triggered or accepted the action, `agent` for a fully autonomous AI agent, `workflow` for a user-created workflow that ran autonomously, and `rule` for an autonomous rule that fired on a trigger. `null` for legacy events.",
        ),
    ] = None
    """
    The type of actor responsible for the event. `user` for a human who directly triggered or accepted the action, `agent` for a fully autonomous AI agent, `workflow` for a user-created workflow that ran autonomously, and `rule` for an autonomous rule that fired on a trigger. `null` for legacy events.
    """

    actor_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="actorId"),
        pydantic.Field(
            alias="actorId",
            description="Unique identifier of the actor that originated the event. `null` when not available.",
        ),
    ] = None
    """
    Unique identifier of the actor that originated the event. `null` when not available.
    """

    actor_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="actorName"),
        pydantic.Field(
            alias="actorName",
            description="Display name of the actor that originated the event. `null` when not available.",
        ),
    ] = None
    """
    Display name of the actor that originated the event. `null` when not available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
