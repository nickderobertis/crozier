

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trigger_param_spec import TriggerParamSpec
from .trigger_spec_state import TriggerSpecState


class TriggerSpec(UniversalBaseModel):
    """
    Definition of a trigger and its parameters
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Trigger description for what it tests and when it will fire during evaluation
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the trigger as it would appear in a policy document
    """

    parameters: typing.Optional[typing.List[TriggerParamSpec]] = pydantic.Field(default=None)
    """
    The list of parameters that are valid for this trigger
    """

    state: typing.Optional[TriggerSpecState] = pydantic.Field(default=None)
    """
    State of the trigger
    """

    superceded_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of another trigger that supercedes this on functionally if this is deprecated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
