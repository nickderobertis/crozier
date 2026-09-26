

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.serialization import FieldMetadata
from ...types.base_filter_model import BaseFilterModel
from .alerts_lookup_key_model_filter_time_range import AlertsLookupKeyModelFilterTimeRange


class AlertsLookupKeyModelFilter(BaseFilterModel):
    """
    Filter to narrow or manage the search
    """

    time_range: typing_extensions.Annotated[
        typing.Optional[AlertsLookupKeyModelFilterTimeRange],
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
