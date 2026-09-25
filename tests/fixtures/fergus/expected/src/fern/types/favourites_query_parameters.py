

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .favourites_query_parameters_representation import FavouritesQueryParametersRepresentation
from .favourites_query_parameters_sort_field import FavouritesQueryParametersSortField
from .favourites_query_parameters_sort_order import FavouritesQueryParametersSortOrder


class FavouritesQueryParameters(UniversalBaseModel):
    page_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[FavouritesQueryParametersSortOrder],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder"),
    ] = None
    page_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageCursor"), pydantic.Field(alias="pageCursor")
    ] = None
    filter_section_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="filterSectionName"),
        pydantic.Field(
            alias="filterSectionName",
            description="Searchable fields:\n- representation: tree\n  - `section.name`\n- representation: flat\n  - `section.name`",
        ),
    ] = None
    """
    Searchable fields:
    - representation: tree
      - `section.name`
    - representation: flat
      - `section.name`
    """

    sort_field: typing_extensions.Annotated[
        typing.Optional[FavouritesQueryParametersSortField],
        FieldMetadata(alias="sortField"),
        pydantic.Field(alias="sortField"),
    ] = None
    representation: typing.Optional[FavouritesQueryParametersRepresentation] = None
    filter_search_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="filterSearchText"),
        pydantic.Field(
            alias="filterSearchText",
            description="Searchable fields:\n- representation: tree\n  - `section.name`\n  - `lineItem.itemName`,\n- representation: flat\n  - `section.name`\n  - `section.description`,\n  - `lineItem.itemName`",
        ),
    ] = None
    """
    Searchable fields:
    - representation: tree
      - `section.name`
      - `lineItem.itemName`,
    - representation: flat
      - `section.name`
      - `section.description`,
      - `lineItem.itemName`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
