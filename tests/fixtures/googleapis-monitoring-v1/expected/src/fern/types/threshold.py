

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .threshold_color import ThresholdColor
from .threshold_direction import ThresholdDirection
from .threshold_target_axis import ThresholdTargetAxis


class Threshold(UniversalBaseModel):
    """
    Defines a threshold for categorizing time series values.
    """

    color: typing.Optional[ThresholdColor] = pydantic.Field(default=None)
    """
    The state color for this threshold. Color is not allowed in a XyChart.
    """

    direction: typing.Optional[ThresholdDirection] = pydantic.Field(default=None)
    """
    The direction for the current threshold. Direction is not allowed in a XyChart.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    A label for the threshold.
    """

    target_axis: typing_extensions.Annotated[
        typing.Optional[ThresholdTargetAxis],
        FieldMetadata(alias="targetAxis"),
        pydantic.Field(
            alias="targetAxis",
            description="The target axis to use for plotting the threshold. Target axis is not allowed in a Scorecard.",
        ),
    ] = None
    """
    The target axis to use for plotting the threshold. Target axis is not allowed in a Scorecard.
    """

    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    The value of the threshold. The value should be defined in the native scale of the metric.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
