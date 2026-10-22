

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .webhook_source import WebhookSource
from .webhook_triggers_item import WebhookTriggersItem


class Webhook(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the webhook
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the webhook
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the webhook was created"),
    ]
    """
    The date and time the webhook was created
    """

    updated_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the webhook was last updated"),
    ]
    """
    The date and time the webhook was last updated
    """

    url: str = pydantic.Field()
    """
    The URL of the webhook
    """

    source: WebhookSource = pydantic.Field()
    """
    The source of the webhook
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The ID of the Workspace"),
    ]
    """
    The ID of the Workspace
    """

    environment_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="environmentId"),
        pydantic.Field(alias="environmentId", description="Deprecated alias for workspaceId."),
    ]
    """
    Deprecated alias for workspaceId.
    """

    triggers: typing.List[WebhookTriggersItem] = pydantic.Field()
    """
    The triggers of the webhook
    """

    survey_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="surveyIds"),
        pydantic.Field(alias="surveyIds", description="The IDs of the surveys "),
    ]
    """
    The IDs of the surveys 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
