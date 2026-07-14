

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trigger_param_spec_state import TriggerParamSpecState


class TriggerParamSpec(UniversalBaseModel):
    description: typing.Optional[str] = None
    example: typing.Optional[str] = pydantic.Field(default=None)
    """
    An example value for the parameter (encoded as a string if the parameter is an object or list type)
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Parameter name as it appears in policy document
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is this a required parameter or optional
    """

    state: typing.Optional[TriggerParamSpecState] = pydantic.Field(default=None)
    """
    State of the trigger parameter
    """

    superceded_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of another trigger that supercedes this on functionally if this is deprecated
    """

    validator: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    If present, a definition for validation of input. Typically a jsonschema object that can be used to validate an input against.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
