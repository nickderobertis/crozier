

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .survey_create_response_payload import SurveyCreateResponsePayload


class SurveyCreateResponse(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    desc: str
    payload: SurveyCreateResponsePayload
    feed_channel_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="feedChannelIds"), pydantic.Field(alias="feedChannelIds")
    ]
    feed_template: typing_extensions.Annotated[
        str, FieldMetadata(alias="feedTemplate"), pydantic.Field(alias="feedTemplate")
    ]
    webhook_url: typing_extensions.Annotated[str, FieldMetadata(alias="webhookUrl"), pydantic.Field(alias="webhookUrl")]
    recent_suggestion_category: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="recentSuggestionCategory"),
        pydantic.Field(alias="recentSuggestionCategory"),
    ]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
