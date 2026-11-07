

import typing

from .source_metronome_config import SourceMetronomeConfig
from .source_postgres_config import SourcePostgresConfig
from .source_stripe_config import SourceStripeConfig

ControlMessageControlSourceConfigSourceConfig = typing.Union[
    SourceStripeConfig, SourcePostgresConfig, SourceMetronomeConfig
]
