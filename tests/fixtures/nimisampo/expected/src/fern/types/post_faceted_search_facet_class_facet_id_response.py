

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .post_faceted_search_facet_class_facet_id_response_data import PostFacetedSearchFacetClassFacetIdResponseData


class PostFacetedSearchFacetClassFacetIdResponse(UniversalBaseModel):
    data: typing.Optional[PostFacetedSearchFacetClassFacetIdResponseData] = pydantic.Field(default=None)
    """
    Facet values as an array of objects (checkbox facets) or as a single object (timespan facets).
    """

    flat_data: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="flatData"),
        pydantic.Field(alias="flatData", description="Facet values as an array of objects with no hierarchy"),
    ] = None
    """
    Facet values as an array of objects with no hierarchy
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of facet
    """

    sparql_query: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sparqlQuery"),
        pydantic.Field(alias="sparqlQuery", description="The SPARQL query that was used for the values of the facet"),
    ] = None
    """
    The SPARQL query that was used for the values of the facet
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
