

import typing

from .citus_subscribe_op_spec_payload_zero import CitusSubscribeOpSpecPayloadZero

CitusSubscribeOpSpecPayload = typing.Union[CitusSubscribeOpSpecPayloadZero, typing.List[str]]
