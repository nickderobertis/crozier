

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .document import Document
from .parse_metadata import ParseMetadata


class ParseResponse(UniversalBaseModel):
    """
    The parse result: the full document as `markdown`, its hierarchical
    `structure` (with per-node spatial `grounding` inline), and request
    `metadata`.
    """

    markdown: str = pydantic.Field()
    """
    The full document as a single Markdown string, in reading order.
    """

    metadata: ParseMetadata = pydantic.Field()
    """
    Information about the request: model version, page count, duration, billing, and more.
    """

    structure: Document = pydantic.Field()
    """
    The document's hierarchical structure: pages and the elements detected on each page. Every node below the root carries its spatial data inline in a `grounding` object (`{page, range, box}`, normalized page coordinates); leaf elements additionally carry `atomic_grounding`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ParseResponse)
