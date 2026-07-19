

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .timerange import Timerange


class FlowSegmentBulkFailureFailedSegmentsItem(UniversalBaseModel):
    """
    Failed Segment details
    """

    object_id: str = pydantic.Field()
    """
    The Object ID of the Segment which has failed to register with the service instance
    """

    timerange: typing.Optional[Timerange] = pydantic.Field(default=None)
    """
    The timerange of Segment that has failed, as described by the [TimeRange](#/schemas/timerange) type
    """

    error: typing.Optional[Error] = pydantic.Field(default=None)
    """
    Provides more information for the error status, as described by the [Error](#/schemas/error) type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
