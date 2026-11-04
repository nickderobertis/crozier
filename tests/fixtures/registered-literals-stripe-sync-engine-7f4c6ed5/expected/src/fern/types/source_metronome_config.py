

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SourceMetronomeConfig(UniversalBaseModel):
    api_key: str = pydantic.Field()
    """
    Metronome API bearer token
    """

    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Override the Metronome API base URL (default: https://api.metronome.com)
    """

    rate_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max requests per second (default: no limit)
    """

    backfill_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max records to fetch per stream (useful for testing)
    """

    webhook_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Webhook signing secret for HMAC-SHA256 signature verification
    """

    webhook_port: typing.Optional[int] = pydantic.Field(default=None)
    """
    Port for built-in webhook HTTP listener (e.g. 4243)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
