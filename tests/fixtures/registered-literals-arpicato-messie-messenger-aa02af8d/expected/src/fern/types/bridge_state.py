

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bridge_state_state_event import BridgeStateStateEvent


class BridgeState(UniversalBaseModel):
    """
    The connection status of an individual login
    """

    state_event: BridgeStateStateEvent = pydantic.Field()
    """
    The current state of this login.
    """

    timestamp: float = pydantic.Field()
    """
    The time when the state was last updated.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    An error code defined by the network connector.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable error message defined by the network connector.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    A reason code for non-error states that aren't exactly successes either.
    """

    info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional arbitrary info provided by the network connector.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
