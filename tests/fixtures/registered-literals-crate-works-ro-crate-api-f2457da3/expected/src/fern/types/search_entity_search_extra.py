

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment import Segment


class SearchEntitySearchExtra(UniversalBaseModel):
    """
    Extra search-related metadata.
    """

    score: typing.Optional[float] = pydantic.Field(default=None)
    """
    The relevance score for this entity, based on the search.
    """

    highlight: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    Selected text snippets from fields matching the query, which can be displayed to users for context. Matched terms are marked within each snippet; this specification is implementation-neutral about the specific mark tag (the examples use `<em>`).
    """

    segments: typing.Optional[typing.List[Segment]] = pydantic.Field(default=None)
    """
    Part of the `segments` extension — see the [Extensions guide](https://ro-crate-api.crate-works.org/docs/extensions). Only present when the implementation declares the `segments` extension in `/capabilities`.
    
    Locations inside the file where the full-text match occurred, allowing clients to deep-link the user to the match (e.g. a PDF page or an ELAN annotation's time range). Segments are optional — absent or empty for hits without structured content. They are ranked by relevance and capped at an implementation-defined limit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
