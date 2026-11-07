

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .source_stripe_config_api_version import SourceStripeConfigApiVersion


class SourceStripeConfig(UniversalBaseModel):
    api_key: str = pydantic.Field()
    """
    Stripe API key (sk_test_... or sk_live_...)
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stripe account ID (resolved from API if omitted)
    """

    account_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    Stripe account creation timestamp in unix seconds (resolved from API if omitted)
    """

    livemode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this is a live mode sync
    """

    api_version: typing.Optional[SourceStripeConfigApiVersion] = None
    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Override the Stripe API base URL (e.g. http://localhost:12111 for stripe-mock)
    """

    webhook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for managed webhook endpoint registration
    """

    webhook_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Webhook signing secret (whsec_...) for signature verification
    """

    websocket: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable WebSocket streaming for live events
    """

    poll_events: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable events API polling for incremental sync after backfill
    """

    webhook_port: typing.Optional[int] = pydantic.Field(default=None)
    """
    Port for built-in webhook HTTP listener (e.g. 4242)
    """

    revalidate_objects: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Object types to re-fetch from Stripe API on webhook (e.g. ["subscription"])
    """

    backfill_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max objects to backfill per stream (useful for testing)
    """

    rate_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Override max requests per second (default: auto-derived from API key mode — 20 live, 10 test).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
