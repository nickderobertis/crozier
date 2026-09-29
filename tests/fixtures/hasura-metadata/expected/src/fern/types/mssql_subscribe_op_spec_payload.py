

import typing

from .mssql_subscribe_op_spec_payload_zero import MssqlSubscribeOpSpecPayloadZero

MssqlSubscribeOpSpecPayload = typing.Union[MssqlSubscribeOpSpecPayloadZero, typing.List[str]]
