

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .geometry import Geometry
from .source_provenance import SourceProvenance
from .table_cell_role import TableCellRole
from .text_span import TextSpan


class TableCell(UniversalBaseModel):
    id: str
    row_index: int
    column_index: int
    row_span: int
    column_span: int
    role: TableCellRole
    text: str
    spans: typing.List[TextSpan]
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    element_ids: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
