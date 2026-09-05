

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .query_parameter_types import QueryParameterTypes
from .query_parameters import QueryParameters
from .read_batch_query import ReadBatchQuery


class ReadQueryRequest(UniversalBaseModel):
    query_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional diagnostic name. It does not create a stored endpoint.
    """

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


update_forward_refs(ReadQueryRequest)
