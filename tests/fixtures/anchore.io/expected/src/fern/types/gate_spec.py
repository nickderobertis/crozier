

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gate_spec_state import GateSpecState
from .trigger_spec import TriggerSpec


class GateSpec(UniversalBaseModel):
    """
    A description of the set of gates available in this engine and the triggers and parameters supported
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the gate
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Gate name, as it would appear in a policy document
    """

    state: typing.Optional[GateSpecState] = pydantic.Field(default=None)
    """
    State of the gate and transitively all triggers it contains if not 'active'
    """

    superceded_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of another trigger that supercedes this on functionally if this is deprecated
    """

    triggers: typing.Optional[typing.List[TriggerSpec]] = pydantic.Field(default=None)
    """
    List of the triggers that can fire for this Gate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
