

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_citation import ExtractionCitation
from .extraction_grounding_field_transform_claim import ExtractionGroundingFieldTransformClaim


class ExtractionGroundingField(UniversalBaseModel):
    """
    Grounding metadata for one leaf in the unwrapped extraction output. `path` uses
    dot-separated property segments and decimal array-index segments, for example
    `line_items.0.amount`.
    """

    path: str = pydantic.Field()
    """
    Dot-separated path from the output root. Array positions are decimal segments.
    Property names containing dots are outside the field-grounding schema subset.
    """

    citations: typing.List[ExtractionCitation]
    dropped_source_ids: typing.Optional[typing.List[str]] = None
    confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    The model's own confidence in this value, 0 to 1, when it reported one. This is a
    self-report, not a calibrated probability, and lineage keeps it labelled as such.
    Omitted when the model reported nothing.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    One or two sentences from the model explaining why the quote is the source for this
    value: what in the document identifies it. This covers the read only; a rewrite is
    reported separately in `transform_claim`. Omitted when none was recorded.
    """

    quote: typing.Optional[str] = pydantic.Field(default=None)
    """
    The span of document text the model says this value was read from, copied verbatim.
    Useful when the value was reformatted and so cannot be found in the document as
    written. Like `reason` this is the model's own report. Omitted when none was recorded.
    """

    transform_claim: typing.Optional[ExtractionGroundingFieldTransformClaim] = pydantic.Field(default=None)
    """
    The model's bounded report of a rewrite: operation, parameters, reason, and optional
    low/medium/high ordinal confidence. The claim is untrusted and never authorizes a
    deterministic validator; only explicit request/schema intent can do that.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
