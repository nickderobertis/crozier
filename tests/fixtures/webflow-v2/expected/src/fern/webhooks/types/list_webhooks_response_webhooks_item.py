

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_webhooks_response_webhooks_item_filter import ListWebhooksResponseWebhooksItemFilter
from .list_webhooks_response_webhooks_item_trigger_type import ListWebhooksResponseWebhooksItemTriggerType


class ListWebhooksResponseWebhooksItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the Webhook registration
    """

    trigger_type: typing_extensions.Annotated[
        typing.Optional[ListWebhooksResponseWebhooksItemTriggerType],
        FieldMetadata(alias="triggerType"),
        pydantic.Field(
            alias="triggerType",
            description="The type of event that triggered the request. See the the documentation for details on [supported events](/data/reference/all-events).",
        ),
    ] = None
    """
    The type of event that triggered the request. See the the documentation for details on [supported events](/data/reference/all-events).
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to send the Webhook payload to
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(
            alias="workspaceId", description="Unique identifier for the Workspace the Webhook is registered in"
        ),
    ] = None
    """
    Unique identifier for the Workspace the Webhook is registered in
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="Unique identifier for the Site the Webhook is registered in"),
    ] = None
    """
    Unique identifier for the Site the Webhook is registered in
    """

    filter: typing.Optional[ListWebhooksResponseWebhooksItemFilter] = pydantic.Field(default=None)
    """
    Only supported for the `form_submission` trigger type. Filter for the form you want Webhooks to be sent for.
    """

    last_triggered: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastTriggered"),
        pydantic.Field(alias="lastTriggered", description="Date the Webhook instance was last triggered"),
    ] = None
    """
    Date the Webhook instance was last triggered
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date the Webhook registration was created"),
    ] = None
    """
    Date the Webhook registration was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
