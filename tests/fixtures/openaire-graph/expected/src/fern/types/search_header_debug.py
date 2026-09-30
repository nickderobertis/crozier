

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .solr_query_params import SolrQueryParams


class SearchHeaderDebug(UniversalBaseModel):
    query_params: typing_extensions.Annotated[
        typing.Optional[SolrQueryParams], FieldMetadata(alias="queryParams"), pydantic.Field(alias="queryParams")
    ] = None
    parsed_query: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parsedQuery"), pydantic.Field(alias="parsedQuery")
    ] = None
    parsed_filter_query: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parsedFilterQuery"), pydantic.Field(alias="parsedFilterQuery")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
