

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .geometry import Geometry
from .source_provenance import SourceProvenance
from .table_cell import TableCell


class TableElement(UniversalBaseModel):
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
