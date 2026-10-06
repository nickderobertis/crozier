

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClientSnapshot(UniversalBaseModel):
    batches_sent: int
    bytes_sent: int
    chunks_sent: int
    connected_at: float
    id: int
    last_write_at: typing.Optional[float] = None
    path: str
    queue_depth: int
    queue_drops: int
    remote_addr: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
