

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .query_parameter_types import QueryParameterTypes
from .query_parameters import QueryParameters
from .read_batch_query import ReadBatchQuery
from .write_batch_query import WriteBatchQuery


class QueryRequest_Read(UniversalBaseModel):
    request_type: typing.Literal["read"] = "read"
    query_name: typing.Optional[str] = None
    query: ReadBatchQuery
    parameters: typing.Optional[QueryParameters] = None
    parameter_types: typing.Optional[QueryParameterTypes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QueryRequest_Write(UniversalBaseModel):
    request_type: typing.Literal["write"] = "write"
    query_name: typing.Optional[str] = None
    query: WriteBatchQuery
    parameters: typing.Optional[QueryParameters] = None
    parameter_types: typing.Optional[QueryParameterTypes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


QueryRequest = typing_extensions.Annotated[
    typing.Union[QueryRequest_Read, QueryRequest_Write], pydantic.Field(discriminator="request_type")
]
update_forward_refs(QueryRequest_Read)
update_forward_refs(QueryRequest_Write)
