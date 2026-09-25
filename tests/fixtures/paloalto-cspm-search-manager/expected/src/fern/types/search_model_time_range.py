

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


class SearchModelTimeRange_Absolute(UniversalBaseModel):
    """
    Time Range
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


class SearchModelTimeRange_Relative(UniversalBaseModel):
    """
    Time Range
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


class SearchModelTimeRange_ToNow(UniversalBaseModel):
    """
    Time Range
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


SearchModelTimeRange = typing_extensions.Annotated[
    typing.Union[SearchModelTimeRange_Absolute, SearchModelTimeRange_Relative, SearchModelTimeRange_ToNow],
    pydantic.Field(discriminator="type"),
]
