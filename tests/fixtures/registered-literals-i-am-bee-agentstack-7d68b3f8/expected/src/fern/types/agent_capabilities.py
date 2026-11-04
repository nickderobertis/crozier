

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_extension import AgentExtension


class AgentCapabilities(UniversalBaseModel):
    """
    Defines optional capabilities supported by an agent.
    """

    extensions: typing.Optional[typing.List[AgentExtension]] = None
    push_notifications: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="pushNotifications"), pydantic.Field(alias="pushNotifications")
    ] = None
    state_transition_history: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="stateTransitionHistory"),
        pydantic.Field(alias="stateTransitionHistory"),
    ] = None
    streaming: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
