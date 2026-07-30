

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destination_google_sheets_config import DestinationGoogleSheetsConfig
from .destination_postgres_config import DestinationPostgresConfig
from .destination_redis_config import DestinationRedisConfig
from .destination_stripe_config import DestinationStripeConfig


class DestinationConfig_Postgres(UniversalBaseModel):
    type: typing.Literal["postgres"] = "postgres"
    postgres: DestinationPostgresConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DestinationConfig_GoogleSheets(UniversalBaseModel):
    type: typing.Literal["google_sheets"] = "google_sheets"
    google_sheets: DestinationGoogleSheetsConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DestinationConfig_Stripe(UniversalBaseModel):
    type: typing.Literal["stripe"] = "stripe"
    stripe: DestinationStripeConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DestinationConfig_Redis(UniversalBaseModel):
    type: typing.Literal["redis"] = "redis"
    redis: DestinationRedisConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DestinationConfig = typing_extensions.Annotated[
    typing.Union[
        DestinationConfig_Postgres, DestinationConfig_GoogleSheets, DestinationConfig_Stripe, DestinationConfig_Redis
    ],
    pydantic.Field(discriminator="type"),
]
