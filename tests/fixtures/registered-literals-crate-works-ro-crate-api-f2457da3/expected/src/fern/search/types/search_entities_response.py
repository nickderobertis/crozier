

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .search_entities_response_entities_item import SearchEntitiesResponseEntitiesItem
from .search_entities_response_facets_value_item import SearchEntitiesResponseFacetsValueItem


class SearchEntitiesResponse(UniversalBaseModel):
    """
    A list of entities matching the query, plus optional facets.
    """

    total: int = pydantic.Field()
    """
    Total number of entities (before pagination) matching the query.
    """

    search_time: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="searchTime"),
        pydantic.Field(alias="searchTime", description="The search duration in milliseconds."),
    ]
    """
    The search duration in milliseconds.
    """

    entities: typing.List[SearchEntitiesResponseEntitiesItem]
    facets: typing.Optional[typing.Dict[str, typing.List[SearchEntitiesResponseFacetsValueItem]]] = pydantic.Field(
        default=None
    )
    """
    Contains facet counts for the search. Keys are facet fields, and values are arrays of objects indicating the facet name and count.
    """

    geohash_grid: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="geohashGrid"),
        pydantic.Field(
            alias="geohashGrid",
            description="Present when boundingBox is used with a precision. Contains counts of entities in each geohash area. Keys are geohash values, and values are the count of entities in that area.",
        ),
    ] = None
    """
    Present when boundingBox is used with a precision. Contains counts of entities in each geohash area. Keys are geohash values, and values are the count of entities in that area.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
