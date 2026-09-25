

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .relative_time_range_config_model_relative_time_type import RelativeTimeRangeConfigModelRelativeTimeType
from .relative_time_range_config_model_value import RelativeTimeRangeConfigModelValue


class RelativeTimeRangeConfigModel(UniversalBaseModel):
    relative_time_type: typing_extensions.Annotated[
        typing.Optional[RelativeTimeRangeConfigModelRelativeTimeType],
        FieldMetadata(alias="relativeTimeType"),
        pydantic.Field(alias="relativeTimeType", description="Direction in which to count time. Default = BACKWARD"),
    ] = None
    """
    Direction in which to count time. Default = BACKWARD
    """

    value: RelativeTimeRangeConfigModelValue = pydantic.Field()
    """
    Time range object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
