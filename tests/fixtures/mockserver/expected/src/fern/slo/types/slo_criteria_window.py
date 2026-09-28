

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .slo_criteria_window_type import SloCriteriaWindowType


class SloCriteriaWindow(UniversalBaseModel):
    """
    the time window to evaluate over
    """

    type: typing.Optional[SloCriteriaWindowType] = None
    lookback_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lookbackMillis"),
        pydantic.Field(
            alias="lookbackMillis", description="LOOKBACK: window length ending now (uses the controllable clock)"
        ),
    ] = None
    """
    LOOKBACK: window length ending now (uses the controllable clock)
    """

    from_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="fromEpochMillis"),
        pydantic.Field(alias="fromEpochMillis", description="EXPLICIT: window start in epoch milliseconds"),
    ] = None
    """
    EXPLICIT: window start in epoch milliseconds
    """

    to_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="toEpochMillis"),
        pydantic.Field(alias="toEpochMillis", description="EXPLICIT: window end in epoch milliseconds"),
    ] = None
    """
    EXPLICIT: window end in epoch milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
