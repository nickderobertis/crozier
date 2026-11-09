

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Segment_Page(UniversalBaseModel):
    """
    A location inside a file where a full-text search match occurred, allowing clients to deep-link the user to the match. Part of the `segments` extension.

    Each segment is one of the registered segment types, discriminated by `type`. New segment types are added by revision of this specification; clients MUST skip segments with a `type` value they do not recognise rather than fail.
    """

    type: typing.Literal["page"] = "page"
    page: int
    highlight: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Segment_TimeAlignedAnnotation(UniversalBaseModel):
    """
    A location inside a file where a full-text search match occurred, allowing clients to deep-link the user to the match. Part of the `segments` extension.

    Each segment is one of the registered segment types, discriminated by `type`. New segment types are added by revision of this specification; clients MUST skip segments with a `type` value they do not recognise rather than fail.
    """

    type: typing.Literal["time-aligned-annotation"] = "time-aligned-annotation"
    tier: str
    start_ms: typing_extensions.Annotated[int, FieldMetadata(alias="startMs"), pydantic.Field(alias="startMs")]
    end_ms: typing_extensions.Annotated[int, FieldMetadata(alias="endMs"), pydantic.Field(alias="endMs")]
    highlight: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Segment = typing_extensions.Annotated[
    typing.Union[Segment_Page, Segment_TimeAlignedAnnotation], pydantic.Field(discriminator="type")
]
