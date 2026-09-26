

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_filter_model import BaseFilterModel
from .filter_model_time_range import FilterModelTimeRange


class FilterModel(BaseFilterModel):
    time_range: typing_extensions.Annotated[
        typing.Optional[FilterModelTimeRange],
        FieldMetadata(alias="timeRange"),
        pydantic.Field(alias="timeRange", description="Time range"),
    ] = None
    """
    Time range
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
