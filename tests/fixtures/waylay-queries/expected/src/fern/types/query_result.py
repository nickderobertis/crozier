

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_execution_message import QueryExecutionMessage
from .query_output import QueryOutput
from .query_result_data_item import QueryResultDataItem


class QueryResult(UniversalBaseModel):
    """
    A json data response.

    Uses the format as specified by the
    `render` options of the request (defaults to `COMPACT_WS`).
    '
    """

    data: typing.List[QueryResultDataItem] = pydantic.Field()
    """
    A list of data sets, each with their own time axis. There will be one dataset for each `role` specified in the query (by default a single `input` role).
    
    The data is represented according to the `render`  options in the query (default `COMPACT_WS`).
    """

    query: QueryOutput = pydantic.Field()
    """
    The query that lead to this result.
    """

    messages: typing.List[QueryExecutionMessage]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
