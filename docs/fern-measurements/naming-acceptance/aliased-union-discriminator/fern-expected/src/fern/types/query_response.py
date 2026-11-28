

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueryResponse_Table(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Literal["table"], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = "table"
    row_count: typing_extensions.Annotated[int, FieldMetadata(alias="rowCount"), pydantic.Field(alias="rowCount")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QueryResponse_Graph(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Literal["graph"], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = "graph"
    nodes: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


QueryResponse = typing_extensions.Annotated[
    typing.Union[QueryResponse_Table, QueryResponse_Graph], pydantic.Field(discriminator="schema")
]
