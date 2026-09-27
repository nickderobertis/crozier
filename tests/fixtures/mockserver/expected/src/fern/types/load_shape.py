

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .load_shape_metric import LoadShapeMetric
from .load_shape_type import LoadShapeType
from .ramp_curve import RampCurve


class LoadShape(UniversalBaseModel):
    """
    a declarative named load shape that expands into ordinary stages; only the parameters its 'type' needs are read, the rest are ignored. Use a shape OR an explicit 'stages' list, not both.
    """

    type: LoadShapeType
    metric: typing.Optional[LoadShapeMetric] = None
    curve: typing.Optional[RampCurve] = None
    baseline: typing.Optional[float] = pydantic.Field(default=None)
    """
    SPIKE: the level held before and after the spike
    """

    peak: typing.Optional[float] = pydantic.Field(default=None)
    """
    SPIKE: the level held at the top of the spike
    """

    ramp_up_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rampUpMillis"),
        pydantic.Field(alias="rampUpMillis", description="SPIKE: duration of the baseline to peak ramp"),
    ] = None
    """
    SPIKE: duration of the baseline to peak ramp
    """

    hold_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="holdMillis"),
        pydantic.Field(
            alias="holdMillis",
            description="SPIKE: duration to hold at the peak; RAMP_HOLD: duration to hold at the target",
        ),
    ] = None
    """
    SPIKE: duration to hold at the peak; RAMP_HOLD: duration to hold at the target
    """

    ramp_down_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rampDownMillis"),
        pydantic.Field(alias="rampDownMillis", description="SPIKE: duration of the peak to baseline ramp"),
    ] = None
    """
    SPIKE: duration of the peak to baseline ramp
    """

    recovery_hold_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="recoveryHoldMillis"),
        pydantic.Field(
            alias="recoveryHoldMillis", description="SPIKE (optional): duration to hold at baseline after the down ramp"
        ),
    ] = None
    """
    SPIKE (optional): duration to hold at baseline after the down ramp
    """

    start: typing.Optional[float] = pydantic.Field(default=None)
    """
    STAIRS: the level of the first step
    """

    step: typing.Optional[float] = pydantic.Field(default=None)
    """
    STAIRS: how much each step rises above the previous one
    """

    steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    STAIRS: the number of steps
    """

    step_duration_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="stepDurationMillis"),
        pydantic.Field(alias="stepDurationMillis", description="STAIRS: how long each step holds at its level"),
    ] = None
    """
    STAIRS: how long each step holds at its level
    """

    target: typing.Optional[float] = pydantic.Field(default=None)
    """
    RAMP_HOLD: the level ramped up to (from 0) and then held
    """

    ramp_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rampMillis"),
        pydantic.Field(alias="rampMillis", description="RAMP_HOLD: duration of the 0 to target ramp"),
    ] = None
    """
    RAMP_HOLD: duration of the 0 to target ramp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
