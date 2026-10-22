

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_summary import MessageSummary
from .paginated_messages_response_object import PaginatedMessagesResponseObject
from .pagination_info import PaginationInfo


class PaginatedMessagesResponse(UniversalBaseModel):
    object: PaginatedMessagesResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[MessageSummary] = pydantic.Field()
    """
    Array of message summaries (content and content_parsed fields omitted for performance)
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
