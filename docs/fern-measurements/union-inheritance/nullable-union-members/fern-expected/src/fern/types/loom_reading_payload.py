

import typing

from .loom_reading_payload_zero import LoomReadingPayloadZero

LoomReadingPayload = typing.Union[typing.Optional[LoomReadingPayloadZero], typing.Optional[str]]
