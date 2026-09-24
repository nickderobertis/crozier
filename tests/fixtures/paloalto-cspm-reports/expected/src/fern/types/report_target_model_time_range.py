

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .absolute_time_range_config_model_value import AbsoluteTimeRangeConfigModelValue
from .relative_time_range_config_model_relative_time_type import RelativeTimeRangeConfigModelRelativeTimeType
from .relative_time_range_config_model_value import RelativeTimeRangeConfigModelValue
from .to_now_time_range_config_model_value import ToNowTimeRangeConfigModelValue


class ReportTargetModelTimeRange_Absolute(UniversalBaseModel):
    """
    Time range
    """

    type: typing.Literal["absolute"] = "absolute"
    value: AbsoluteTimeRangeConfigModelValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ReportTargetModelTimeRange_Relative(UniversalBaseModel):
    """
    Time range
    """

    type: typing.Literal["relative"] = "relative"
    relative_time_type: typing_extensions.Annotated[
        typing.Optional[RelativeTimeRangeConfigModelRelativeTimeType],
        FieldMetadata(alias="relativeTimeType"),
        pydantic.Field(alias="relativeTimeType"),
    ] = None
    value: RelativeTimeRangeConfigModelValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ReportTargetModelTimeRange_ToNow(UniversalBaseModel):
    """
    Time range
    """

    type: typing.Literal["to_now"] = "to_now"
    value: typing.Optional[ToNowTimeRangeConfigModelValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ReportTargetModelTimeRange = typing_extensions.Annotated[
    typing.Union[
        ReportTargetModelTimeRange_Absolute, ReportTargetModelTimeRange_Relative, ReportTargetModelTimeRange_ToNow
    ],
    pydantic.Field(discriminator="type"),
]
