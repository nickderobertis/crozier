

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destination_stripe_config_api_version import DestinationStripeConfigApiVersion
from .destination_stripe_config_object import DestinationStripeConfigObject
from .destination_stripe_config_streams_value import DestinationStripeConfigStreamsValue
from .destination_stripe_config_write_mode import DestinationStripeConfigWriteMode


class DestinationStripeConfig(UniversalBaseModel):
    api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stripe API key (sk_test_... or sk_live_...)
    """

    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Override the Stripe API base URL (e.g. http://localhost:12111 for tests)
    """

    max_retries: typing.Optional[int] = pydantic.Field(default=None)
    """
    Retries for 429/5xx/network errors
    """

    api_version: typing.Optional[DestinationStripeConfigApiVersion] = None
    object: typing.Optional[DestinationStripeConfigObject] = None
    write_mode: typing.Optional[DestinationStripeConfigWriteMode] = None
    streams: typing.Optional[typing.Dict[str, DestinationStripeConfigStreamsValue]] = pydantic.Field(default=None)
    """
    Per-source-stream Custom Object write configuration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
