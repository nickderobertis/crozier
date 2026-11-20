

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReaderInfo(UniversalBaseModel):
    """
    One principal who READ ``dataset`` — the access-audit twin of :class:`ProducerInfo` (who WROTE it).

    Aggregated per reader: the verified subject, when they last read it, and how many times. Sourced from
    the append-only ``lineage_reads`` audit log (#6/#41), not the AGE graph — reads are access events, not
    provenance edges, so they never mint a graph vertex.
    """

    last_read: typing.Optional[str] = None
    reader: str
    reads: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
