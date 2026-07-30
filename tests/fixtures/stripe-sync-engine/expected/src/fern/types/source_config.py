

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .source_metronome_config import SourceMetronomeConfig
from .source_postgres_config import SourcePostgresConfig
from .source_stripe_config import SourceStripeConfig


class SourceConfig_Stripe(UniversalBaseModel):
    type: typing.Literal["stripe"] = "stripe"
    stripe: SourceStripeConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SourceConfig_Postgres(UniversalBaseModel):
    type: typing.Literal["postgres"] = "postgres"
    postgres: SourcePostgresConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SourceConfig_Metronome(UniversalBaseModel):
    type: typing.Literal["metronome"] = "metronome"
    metronome: SourceMetronomeConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SourceConfig = typing_extensions.Annotated[
    typing.Union[SourceConfig_Stripe, SourceConfig_Postgres, SourceConfig_Metronome],
    pydantic.Field(discriminator="type"),
]
