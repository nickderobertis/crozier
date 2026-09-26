

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tic_search_result import TicSearchResult


class TicSearchResponse(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="$schema"),
        pydantic.Field(alias="$schema", description="URL to the JSON Schema for this response"),
    ]
    """
    URL to the JSON Schema for this response
    """

    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(alias="nextCursor", description="Cursor for retrieving the next page of results"),
    ] = None
    """
    Cursor for retrieving the next page of results
    """

    query: str = pydantic.Field()
    """
    Echo of the input query
    """

    results: typing.Optional[typing.List[TicSearchResult]] = pydantic.Field(default=None)
    """
    Ranked TIC results (most relevant first)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
