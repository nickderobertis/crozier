

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InlineResponse2003Value(UniversalBaseModel):
    """
    The current value for a config, which includes the name, value, recommended values, etc.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the configuration
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value for the configuration
    """

    recommended_values: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of valid values for the configuration
    """

    errors: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Errors, if any, in the configuration value
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The visibility of the configuration. Based on the values of other configuration
    fields, this visibility boolean value points out if the current field should be
    visible or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
