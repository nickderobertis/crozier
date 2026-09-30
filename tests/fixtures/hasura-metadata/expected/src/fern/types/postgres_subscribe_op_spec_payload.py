

import typing

from .postgres_subscribe_op_spec_payload_zero import PostgresSubscribeOpSpecPayloadZero

PostgresSubscribeOpSpecPayload = typing.Union[PostgresSubscribeOpSpecPayloadZero, typing.List[str]]
