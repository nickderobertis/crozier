

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_activity_logs_response_items_item import ListActivityLogsResponseItemsItem
from .list_activity_logs_response_pagination import ListActivityLogsResponsePagination


class ListActivityLogsResponse(UniversalBaseModel):
    items: typing.Optional[typing.List[ListActivityLogsResponseItemsItem]] = None
    pagination: typing.Optional[ListActivityLogsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
