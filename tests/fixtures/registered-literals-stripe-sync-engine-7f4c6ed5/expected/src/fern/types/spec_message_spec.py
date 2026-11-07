

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpecMessageSpec(UniversalBaseModel):
    """
    JSON Schema describing the configuration a connector requires.
    """

    config: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    JSON Schema for the connector's configuration object.
    """

    source_state_stream: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON Schema for per-stream state (cursor/checkpoint shape). See also SourceState.global for sync-wide cursors.
    """

    source_input: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON Schema for the read() input parameter (e.g. a webhook event).
    """

    soft_limit_fraction: typing.Optional[float] = pydantic.Field(default=None)
    """
    Fraction of `time_limit` to use as default `soft_time_limit` (e.g. 0.5).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
