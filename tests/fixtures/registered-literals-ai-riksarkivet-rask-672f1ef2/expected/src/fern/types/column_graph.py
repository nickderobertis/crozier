

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column_edge import ColumnEdge
from .column_node import ColumnNode


class ColumnGraph(UniversalBaseModel):
    """
    The column-level lineage subgraph around ``root`` (nodes + edges) — the column analogue of the
    dataset ``LineageGraph``, for a field-to-field DAG view.
    """

    columns: typing.Optional[typing.List[ColumnNode]] = None
    edges: typing.Optional[typing.List[ColumnEdge]] = None
    root: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
