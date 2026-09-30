

import typing

from .cockroach_subscribe_op_spec_payload_zero import CockroachSubscribeOpSpecPayloadZero

CockroachSubscribeOpSpecPayload = typing.Union[CockroachSubscribeOpSpecPayloadZero, typing.List[str]]
