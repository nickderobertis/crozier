

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_webhook_response_source import GetWebhookResponseSource
from .get_webhook_response_triggers_item import GetWebhookResponseTriggersItem


class GetWebhookResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the webhook
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the webhook
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the webhook was created"),
    ] = None
    """
    The date and time the webhook was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the webhook was last updated"),
    ] = None
    """
    The date and time the webhook was last updated
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the webhook
    """

    source: typing.Optional[GetWebhookResponseSource] = pydantic.Field(default=None)
    """
    The source of the webhook
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The ID of the Workspace"),
    ] = None
    """
    The ID of the Workspace
    """

    environment_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="environmentId"),
        pydantic.Field(alias="environmentId", description="Deprecated alias for workspaceId."),
    ] = None
    """
    Deprecated alias for workspaceId.
    """

    triggers: typing.Optional[typing.List[GetWebhookResponseTriggersItem]] = pydantic.Field(default=None)
    """
    The triggers of the webhook
    """

    survey_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="surveyIds"),
        pydantic.Field(alias="surveyIds", description="The IDs of the surveys "),
    ] = None
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
