

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_info_supported_parameter_allowed_values_item import ModelInfoSupportedParameterAllowedValuesItem
from .model_info_supported_parameter_default import ModelInfoSupportedParameterDefault


class ModelInfoSupportedParameter(UniversalBaseModel):
    """
    Describes a parameter supported by the model, including parameter value constraints.
    """

    parameter: str = pydantic.Field()
    """
    The name of the parameter.
    """

    type: str = pydantic.Field()
    """
    The parameter type e.g. 'one_of', 'numeric_range', or 'any'.
    
    If the type is 'one_of', then 'allowed_values' will be set, and the value specified must be one of the allowed values. 'one_of' is only compatible with value_type 'string' or 'integer'.
    
    If 'numeric_range', then 'min' and 'max' will be set, then the value specified must adhere to the value_type and must fall within the `[min, max]` range (inclusive).
    
    If 'any' then any value is allowed, as long as it adheres to the value_type.
    """

    value_type: str = pydantic.Field()
    """
    The type of value the parameter accepts, e.g. 'string', 'integer', 'float', or 'boolean'.
    """

    required: bool = pydantic.Field()
    """
    Whether the parameter is required (true) or optional (false).
    """

    allowed_values: typing.Optional[typing.List[ModelInfoSupportedParameterAllowedValuesItem]] = pydantic.Field(
        default=None
    )
    """
    The allowed parameter values when the type is 'one_of'.
    """

    min: typing.Optional[float] = pydantic.Field(default=None)
    """
    The minimum allowed value (inclusive) when the type is 'numeric_range'.
    """

    max: typing.Optional[float] = pydantic.Field(default=None)
    """
    The maximum allowed value (inclusive) when the type is 'numeric_range'.
    """

    default: typing.Optional[ModelInfoSupportedParameterDefault] = pydantic.Field(default=None)
    """
    The default value for the parameter when a parameter is optional.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
