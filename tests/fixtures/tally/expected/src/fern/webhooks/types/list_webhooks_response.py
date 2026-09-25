

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_webhooks_response_webhooks_item import ListWebhooksResponseWebhooksItem


class ListWebhooksResponse(UniversalBaseModel):
    webhooks: typing.Optional[typing.List[ListWebhooksResponseWebhooksItem]] = pydantic.Field(default=None)
    """
    List of webhooks
    """

    page: typing.Optional[float] = pydantic.Field(default=None)
    """
    Current page number
    """

    limit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of webhooks per page
    """

    has_more: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMore"),
        pydantic.Field(alias="hasMore", description="Whether there are more pages available"),
    ] = None
    """
    Whether there are more pages available
    """

    total_count: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="Total number of webhooks"),
    ] = None
    """
    Total number of webhooks
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
