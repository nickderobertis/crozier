

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .result_intent_zero_add_annotations_source import ResultIntentZeroAddAnnotationsSource
from .result_intent_zero_add_segment_group_segments_item import ResultIntentZeroAddSegmentGroupSegmentsItem
from .result_intent_zero_add_segment_group_source import ResultIntentZeroAddSegmentGroupSource


class ResultIntentZero_AddBaseImage(UniversalBaseModel):
    intent: typing.Literal["add-base-image"] = "add-base-image"
    id: str
    name: str
    url: str
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    size: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResultIntentZero_AddLayer(UniversalBaseModel):
    intent: typing.Literal["add-layer"] = "add-layer"
    id: str
    name: str
    url: str
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    size: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResultIntentZero_AddSegmentGroup(UniversalBaseModel):
    intent: typing.Literal["add-segment-group"] = "add-segment-group"
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


class ResultIntentZero_AddAnnotations(UniversalBaseModel):
    intent: typing.Literal["add-annotations"] = "add-annotations"
    id: str
    name: str
    url: str
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    size: typing.Optional[float] = None
    source: typing.Optional[ResultIntentZeroAddAnnotationsSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResultIntentZero = typing_extensions.Annotated[
    typing.Union[
        ResultIntentZero_AddBaseImage,
        ResultIntentZero_AddLayer,
        ResultIntentZero_AddSegmentGroup,
        ResultIntentZero_AddAnnotations,
    ],
    pydantic.Field(discriminator="intent"),
]
