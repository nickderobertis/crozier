

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueryRun(UniversalBaseModel):
    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="A URL to access this query run"),
    ] = None
    """
    A URL to access this query run
    """

    query_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="QueryURI"),
        pydantic.Field(alias="QueryURI", description="A URL to access the query that was run"),
    ] = None
    """
    A URL to access the query that was run
    """

    run_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="RunTime"), pydantic.Field(alias="RunTime")
    ] = None
    query_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="QueryID"),
        pydantic.Field(
            alias="QueryID", description="A reference to an object in the queries property identified by QueryID"
        ),
    ] = None
    """
    A reference to an object in the queries property identified by QueryID
    """

    query_run_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="QueryRunID"),
        pydantic.Field(alias="QueryRunID", description="A reference to the run number of this query"),
    ] = None
    """
    A reference to the run number of this query
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
