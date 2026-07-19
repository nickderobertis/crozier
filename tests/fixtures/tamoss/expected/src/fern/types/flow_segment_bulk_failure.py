

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_segment_bulk_failure_failed_segments_item import FlowSegmentBulkFailureFailedSegmentsItem


class FlowSegmentBulkFailure(UniversalBaseModel):
    """
    List of Segments that have failed to register
    """

    failed_segments: typing.List[FlowSegmentBulkFailureFailedSegmentsItem] = pydantic.Field()
    """
    The list of Segments which have failed to register with the service instance
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
