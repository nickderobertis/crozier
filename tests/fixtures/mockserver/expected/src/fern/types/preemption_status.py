

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preemption_status_mode import PreemptionStatusMode
from .preemption_status_state import PreemptionStatusState


class PreemptionStatus(UniversalBaseModel):
    """
    current cordon/drain status of the server
    """

    state: typing.Optional[PreemptionStatusState] = None
    in_flight: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="inFlight"),
        pydantic.Field(alias="inFlight", description="number of requests currently in flight"),
    ] = None
    """
    number of requests currently in flight
    """

    drain_remaining_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="drainRemainingMillis"),
        pydantic.Field(alias="drainRemainingMillis", description="milliseconds left in the drain window"),
    ] = None
    """
    milliseconds left in the drain window
    """

    mode: typing.Optional[PreemptionStatusMode] = pydantic.Field(default=None)
    """
    active signalling mode (omitted when inactive)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
