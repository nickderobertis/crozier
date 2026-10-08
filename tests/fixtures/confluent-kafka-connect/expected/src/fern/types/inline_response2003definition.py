

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inline_response2003definition_importance import InlineResponse2003DefinitionImportance
from .inline_response2003definition_type import InlineResponse2003DefinitionType
from .inline_response2003definition_width import InlineResponse2003DefinitionWidth


class InlineResponse2003Definition(UniversalBaseModel):
    """
    The definition for a config in the connector plugin, which includes the name, type, importance, etc.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the configuration
    """

    type: typing.Optional[InlineResponse2003DefinitionType] = pydantic.Field(default=None)
    """
    The config types
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this configuration is required
    """

    default_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default value for this configuration
    """

    importance: typing.Optional[InlineResponse2003DefinitionImportance] = pydantic.Field(default=None)
    """
    The importance level for a configuration
    """

    documentation: typing.Optional[str] = pydantic.Field(default=None)
    """
    The documentation for the configuration
    """

    group: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UI group to which the configuration belongs to
    """

    width: typing.Optional[InlineResponse2003DefinitionWidth] = pydantic.Field(default=None)
    """
    The width of a configuration value
    """

    display_name: typing.Optional[str] = None
    dependents: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Other configurations on which this configuration is dependent
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    The order of configuration in specified group
    """

    alias: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
