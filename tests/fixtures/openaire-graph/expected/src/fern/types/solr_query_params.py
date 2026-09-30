

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sort_clause import SortClause


class SolrQueryParams(UniversalBaseModel):
    query_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="queryString"), pydantic.Field(alias="queryString")
    ] = None
    filter_queries: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="filterQueries"), pydantic.Field(alias="filterQueries")
    ] = None
    field_list: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fieldList"), pydantic.Field(alias="fieldList")
    ] = None
    debug_query: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="debugQuery"), pydantic.Field(alias="debugQuery")
    ] = None
    start: typing.Optional[int] = None
    rows: typing.Optional[int] = None
    sort: typing.Optional[typing.List[SortClause]] = None
    cursor: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
