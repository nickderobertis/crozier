

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transport_snapshot_mode import TransportSnapshotMode


class TransportSnapshot(UniversalBaseModel):
    auth_failures: int
    auth_successes: int
    configurable: bool
    contract_version: int
    key_ids: typing.List[str]
    mode: TransportSnapshotMode
    port: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
