

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pagination_response import PaginationResponse
from .query import Query


class GetQueriesResponse(UniversalBaseModel):
    queries: typing.List[Query] = pydantic.Field()
    """
    List of queries matching the request criteria
    """

    pagination: PaginationResponse = pydantic.Field()
    """
    Pagination information
    """

    conversation_resolutions: typing.Optional[typing.Dict[str, bool]] = pydantic.Field(default=None)
    """
    Whether each conversation in `queries` was resolved. Conversations the resolution job has not scored yet are absent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
