

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_webhooks_response_pagination import ListWebhooksResponsePagination
from .list_webhooks_response_webhooks_item import ListWebhooksResponseWebhooksItem


class ListWebhooksResponse(UniversalBaseModel):
    webhooks: typing.Optional[typing.List[ListWebhooksResponseWebhooksItem]] = None
    pagination: typing.Optional[ListWebhooksResponsePagination] = pydantic.Field(default=None)
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
