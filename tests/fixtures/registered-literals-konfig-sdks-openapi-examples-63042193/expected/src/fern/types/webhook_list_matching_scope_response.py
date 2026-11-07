

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_list_matching_scope_response_items_item import WebhookListMatchingScopeResponseItemsItem


class WebhookListMatchingScopeResponse(UniversalBaseModel):
    """
    A list of webhooks
    """

    items: typing.List[WebhookListMatchingScopeResponseItemsItem]
    next_page_token: str = pydantic.Field()
    """
    A token to pass as a `page-token` query parameter to return the next page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
