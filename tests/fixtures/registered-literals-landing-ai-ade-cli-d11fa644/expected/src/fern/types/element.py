

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .element_type import ElementType
from .grounding import Grounding


class Element(UniversalBaseModel):
    """
    Hierarchical document element. All non-page elements share this shape.

    Keys off `type`; optional fields are excluded from the serialized JSON
    via ``exclude_none=True`` when not set.
    """

    type: ElementType = pydantic.Field()
    """
    The element type. Determines which optional fields appear on this element.
    """

    id: str = pydantic.Field()
    """
    Semantic element id, unique within the document. Format `<type>-<index>`, where `<index>` is a per-type 0-based counter assigned in reading order — `text-0` is the first text element in the document, `figure-0` the first figure, `table_cell-0` the first cell of the first table. Stable within a response but not across re-parses of the same document.
    """

    grounding: Grounding = pydantic.Field()
    """
    The element's spatial data: the page it appears on, its `[start, end)` range in the top-level `markdown` string, and its bounding box in normalized page coordinates.
    """

    atomic_grounding: typing.Optional[typing.List[Grounding]] = pydantic.Field(default=None)
    """
    Fine-grained grounding segments at the model's current granularity (visual lines today; finer in future versions, same schema). Present only on leaf elements — every type except `table`. `[]` only when segments are structurally impossible: `table_cell` (a cell has no finer granularity than itself) and elements whose markdown is suppressed via `blocks.<type>.markdown=false`. Any other leaf the model could not segment finer carries a single entry covering the element's full range and box. Omitted entirely when `options.atomic_grounding` is `false`.
    """

    children: typing.Optional[typing.List["Element"]] = pydantic.Field(default=None)
    """
    The cells (`table_cell` elements) of a `table` element. Present only when `type` is `table`.
    """

    markdown: typing.Optional[str] = pydantic.Field(default=None)
    """
    The element's slice of the top-level `markdown` string (`markdown[grounding.range.start:grounding.range.end]`). `""` for zero-length ranges (e.g. blocks suppressed via `blocks.<type>.markdown=false`). Present only when `options.inline_markdown` is `true`.
    """

    row: typing.Optional[int] = pydantic.Field(default=None)
    """
    0-indexed row position of this cell within its parent `table`. Present only on `table_cell` elements.
    """

    col: typing.Optional[int] = pydantic.Field(default=None)
    """
    0-indexed column position of this cell within its parent `table`. Present only on `table_cell` elements.
    """

    colspan: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of columns this cell spans. `1` for unmerged cells. Present only on `table_cell` elements.
    """

    rowspan: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of rows this cell spans. `1` for unmerged cells. Present only on `table_cell` elements.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Element)
