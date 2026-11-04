

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_from_state import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState,
)
from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_to_state import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesToState,
)
from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_trigger import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger,
)


class GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributes(UniversalBaseModel):
    auto: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bool of representing whether a user created the action.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    A comment made explaining the reasoning of the action.
    """

    date_created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the action was created.
    """

    from_state: typing.Optional[
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState
    ] = pydantic.Field(default=None)
    """
    The name of the state of the Schema Response prior to the creation of the action.
    """

    to_state: typing.Optional[
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesToState
    ] = pydantic.Field(default=None)
    """
    The name of the state of the Schema Response after the creation of the action
    """

    trigger: typing.Optional[
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger
    ] = pydantic.Field(default=None)
    """
    The name of the trigger that caused the action.
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bool of representing whether the action is visible.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
