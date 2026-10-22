

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paginated_webhooks_response_object import PaginatedWebhooksResponseObject
from .pagination_info import PaginationInfo
from .webhook import Webhook


class PaginatedWebhooksResponse(UniversalBaseModel):
    object: PaginatedWebhooksResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[Webhook] = pydantic.Field()
    """
    Array of webhooks
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
