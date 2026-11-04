

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributes,
)
from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_links import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseLinks,
)
from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_relationships import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseRelationships,
)


class GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse(UniversalBaseModel):
    attributes: typing.Optional[GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributes] = (
        None
    )
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Schema Response Action.
    """

    links: typing.Optional[GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseLinks] = (
        pydantic.Field(default=None)
    )
    """
    URLs to alternative representations of the Registration Schema entity.
    """

    relationships: typing.Optional[
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseRelationships
    ] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the Schema Response Action entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the Schema Response Action (`schema-response-actions`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
