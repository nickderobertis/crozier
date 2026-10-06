

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message import Message
from .query_list_hal_links import QueryListHalLinks
from .query_list_item import QueryListItem


class QueriesListResponse(UniversalBaseModel):
    """
    Listing of named queries, with paging links.
    """

    messages: typing.Optional[typing.List[Message]] = None
    queries: typing.List[QueryListItem] = pydantic.Field()
    """
    One page of matching query definitions.
    """

    count: int = pydantic.Field()
    """
    Number of query definitions returned in the current response.
    """

    offset: int = pydantic.Field()
    """
    Offset in the full listing (skipped definitions).
    """

    limit: int = pydantic.Field()
    """
    Maximal number of query definitions returned in one response.
    """

    total_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of query definitions matching the filter.
    """

    links: typing_extensions.Annotated[QueryListHalLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
