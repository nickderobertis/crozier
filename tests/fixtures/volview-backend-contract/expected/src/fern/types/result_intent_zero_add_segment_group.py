

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .result_intent_zero_add_segment_group_segments_item import ResultIntentZeroAddSegmentGroupSegmentsItem
from .result_intent_zero_add_segment_group_source import ResultIntentZeroAddSegmentGroupSource


class ResultIntentZeroAddSegmentGroup(UniversalBaseModel):
    id: str
    name: str
    url: str
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    size: typing.Optional[float] = None
    segments: typing.Optional[typing.List[ResultIntentZeroAddSegmentGroupSegmentsItem]] = None
    source: typing.Optional[ResultIntentZeroAddSegmentGroupSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
