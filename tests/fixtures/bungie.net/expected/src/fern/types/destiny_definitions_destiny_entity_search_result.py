

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_result_of_destiny_entity_search_result_item import SearchResultOfDestinyEntitySearchResultItem


class DestinyDefinitionsDestinyEntitySearchResult(UniversalBaseModel):
    """
    The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.
    """

    results: typing.Optional[SearchResultOfDestinyEntitySearchResultItem] = pydantic.Field(default=None)
    """
    The items found that are matches/near matches for the searched-for term, sorted by something vaguely resembling "relevance". Hopefully this will get better in the future.
    """

    suggested_words: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="suggestedWords")
    ] = pydantic.Field(default=None)
    """
    A list of suggested words that might make for better search results, based on the text searched for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
