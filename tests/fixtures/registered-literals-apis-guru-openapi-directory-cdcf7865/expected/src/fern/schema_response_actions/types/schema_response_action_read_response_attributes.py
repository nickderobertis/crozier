

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schema_response_action_read_response_attributes_from_state import (
    SchemaResponseActionReadResponseAttributesFromState,
)
from .schema_response_action_read_response_attributes_to_state import SchemaResponseActionReadResponseAttributesToState
from .schema_response_action_read_response_attributes_trigger import SchemaResponseActionReadResponseAttributesTrigger


class SchemaResponseActionReadResponseAttributes(UniversalBaseModel):
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

    from_state: typing.Optional[SchemaResponseActionReadResponseAttributesFromState] = pydantic.Field(default=None)
    """
    The name of the state of the Schema Response prior to the creation of the action.
    """

    to_state: typing.Optional[SchemaResponseActionReadResponseAttributesToState] = pydantic.Field(default=None)
    """
    The name of the state of the Schema Response after the creation of the action
    """

    trigger: typing.Optional[SchemaResponseActionReadResponseAttributesTrigger] = pydantic.Field(default=None)
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
