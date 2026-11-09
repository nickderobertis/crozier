

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimeAlignedAnnotationSegment(UniversalBaseModel):
    """
    A search match located in a time-aligned annotation, such as an ELAN annotation tier.
    """

    tier: str = pydantic.Field()
    """
    The identifier of the annotation tier the match occurred in (for ELAN, the TIER_ID).
    """

    start_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="startMs"),
        pydantic.Field(
            alias="startMs",
            description="The start of the matching annotation, in milliseconds from the beginning of the media.",
        ),
    ]
    """
    The start of the matching annotation, in milliseconds from the beginning of the media.
    """

    end_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="endMs"),
        pydantic.Field(
            alias="endMs",
            description="The end of the matching annotation, in milliseconds from the beginning of the media.",
        ),
    ]
    """
    The end of the matching annotation, in milliseconds from the beginning of the media.
    """

    highlight: typing.List[str] = pydantic.Field()
    """
    Matched text fragments from this annotation, using the same marking convention as `searchExtra.highlight`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
