

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_callback_metadata import LinkCallbackMetadata
from .plaid_error import PlaidError


class LinkDeliveryCallbackWebhook(UniversalBaseModel):
    """
    Webhook containing metadata proxied over from Link callback e.g `onEvent`, `onExit`, `onSuccess`.
    """

    error: typing.Optional[PlaidError] = None
    link_callback_metadata: LinkCallbackMetadata
    link_delivery_session_id: str = pydantic.Field()
    """
    The ID of the link delivery session.
    """

    timestamp: str = pydantic.Field()
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    webhook_code: str = pydantic.Field()
    """
    `LINK_CALLBACK`
    """

    webhook_type: str = pydantic.Field()
    """
    `LINK_DELIVERY`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
