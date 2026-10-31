

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .formula_format import FormulaFormat
from .geometry import Geometry
from .language import Language
from .section_role import SectionRole
from .selection_mark_type import SelectionMarkType
from .selection_state import SelectionState
from .source_provenance import SourceProvenance
from .structured_value import StructuredValue
from .table_cell import TableCell
from .text_break import TextBreak
from .text_role import TextRole
from .text_span import TextSpan
from .text_style import TextStyle


class DocumentElement_Text(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["text"] = "text"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    role: TextRole
    text: str
    spans: typing.List[TextSpan]
    languages: typing.List[Language]
    style: typing.Optional[TextStyle] = None
    break_after: typing.Optional[TextBreak] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Table(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["table"] = "table"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    row_count: int
    column_count: int
    cells: typing.List[TableCell]
    html: typing.Optional[str] = None
    markdown: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Figure(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["figure"] = "figure"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    asset_id: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    caption_spans: typing.List[TextSpan]
    alt_text: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Formula(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["formula"] = "formula"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    value: str
    format: FormulaFormat
    spans: typing.List[TextSpan]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_KeyValue(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["key_value"] = "key_value"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    key: StructuredValue
    value: StructuredValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_QueryAnswer(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["query_answer"] = "query_answer"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    query: StructuredValue
    answer: typing.Optional[StructuredValue] = None
    alias: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Section(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["section"] = "section"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    role: SectionRole
    title: typing.Optional[str] = None
    spans: typing.List[TextSpan]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_SelectionMark(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["selection_mark"] = "selection_mark"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    state: SelectionState
    mark_type: SelectionMarkType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Signature(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["signature"] = "signature"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    text: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Barcode(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["barcode"] = "barcode"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    value: str
    symbology: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Link(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["link"] = "link"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    url: str
    text: typing.Optional[str] = None
    spans: typing.List[TextSpan]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Stamp(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["stamp"] = "stamp"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    text: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentElement_Other(UniversalBaseModel):
    """
    One semantic node in the `openparser@1` document graph. Elements carry typed payloads
    (text, table, figure, and other kinds), optional geometry in `locations`, and stable `id`
    values referenced by pages, relations, assets, and grounding citations.
    """

    kind: typing.Literal["other"] = "other"
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    label: str
    text: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocumentElement = typing_extensions.Annotated[
    typing.Union[
        DocumentElement_Text,
        DocumentElement_Table,
        DocumentElement_Figure,
        DocumentElement_Formula,
        DocumentElement_KeyValue,
        DocumentElement_QueryAnswer,
        DocumentElement_Section,
        DocumentElement_SelectionMark,
        DocumentElement_Signature,
        DocumentElement_Barcode,
        DocumentElement_Link,
        DocumentElement_Stamp,
        DocumentElement_Other,
    ],
    pydantic.Field(discriminator="kind"),
]
